from pyrnp.util import get_file_from_path
from pyrnp.exception import InvalidFileError

import requests

PLATFORMS = {"eduplay_test": "https://hmg.eduplay.rnp.br/services/", "eduplay": "https://eduplay.rnp.br/services/"}

SUPPORTED_FILETYPES = [
    "mp4",
    "flv",
    "ogv",
    "wmv",
    "avi",
    "webm",
    "3gp",
    "mov",
    "ogg",
    "mkv",
]


class RNP:
    def __init__(
        self,
        client_key: str,
        client_id: str,
        platform: str = "eduplay",
        username: str = None,
        token: str = None,
        oauth: bool = False,
        json: bool = True,
    ):
        self.client_key = client_key
        self.client_id = client_id
        self.username = username
        self.oauth = oauth
        self.token = token
        self.json = json

        if platform not in PLATFORMS:
            raise NameError("Invalid platform selected. Available platforms: eduplay, rnp, rnp_test")
        else:
            self.url = PLATFORMS[platform]

    def get_request(self, api_url: str = None):
        headers = self.get_header(self.oauth)

        if self.json:
            return requests.get(f"{self.url}{api_url}", headers=headers).json()
        else:
            return requests.get(f"{self.url}{api_url}", headers=headers)

    def post_request(
        self,
        api_url: str = None,
        custom_headers: dict = None,
        files: dict = None,
    ):
        headers = self.get_header(self.oauth)

        if custom_headers is not None:
            for k, v in custom_headers.items():
                headers[k] = v

        if "apps.kloud.rnp.br/media/" in api_url:
            full_url = api_url
        else:
            full_url = f"{self.url}{api_url}"

        if self.json:
            return requests.post(full_url, headers=headers, files=files).json()
        else:
            return requests.post(full_url, headers=headers, files=files)

    def get_header(self, is_oauth: bool = None):
        headers = {
            "Accept-Encoding": None,
            "clientKey": self.client_key,
            "User-Agent": "curl/7.68.0",  # Keep this
        }

        if self.oauth and self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def upload(self, filename: str, id: str):
        if filename.split(".")[1] not in SUPPORTED_FILETYPES:
            raise InvalidFileError("This filetype is not supported")

        parsed_filename = get_file_from_path(filename)

        return_data = self.get_request(api_url=f"video/upload/url/{id}/{parsed_filename}")

        if return_data["operationCode"] != 0:
            raise ConnectionError(f"Could not fetch upload URL: {return_data}")

        print(return_data)

        with open(filename, "rb") as f:
            return_data = self.post_request(return_data["result"], files={parsed_filename: f})

        if "files" in return_data:
            return return_data["files"][0]
        else:
            raise ConnectionError("Upload failed: " + return_data)

    def publish(
        self,
        filename: str,
        id: str,
        title: str,
        keywords: str,
        username: str = None,
        thumbnail: str = "thumb.png",
        thumb_file: bytes = None,
    ):
        if not username:
            username = self.username

        if type(thumbnail) == str and thumb_file is None:
            thumb_file = open(thumbnail, "rb")

        video_data = {
            "video": (
                None,
                f"<video><title>{title.replace('&', 'and')}</title><keywords>{keywords.replace('&', 'and')}</keywords></video>",  # noqa: E501
                "text/xml",
            ),
            "file": (thumbnail, thumb_file),
        }

        return_data = self.post_request(
            api_url=f"video/{username}/save/{id}/{get_file_from_path(filename)}",
            files=video_data,
            custom_headers={"Content-Disposition": "attachment;filename="},
        )

        if "operationCode" not in return_data:
            raise NameError(f"Could not publish video: {return_data}")
        elif return_data["operationCode"] == 103:
            raise ConnectionError(f"Could not publish video, error sending metadata: {return_data}")
        elif return_data["operationCode"] != 1:
            raise NameError(f"Could not publish video: {return_data}")

        return return_data

    def change_video(self, filename: str, id: str, username=None):
        if not username:
            username = self.username

        return_data = self.post(api_url=f"video/{username}/change/file/default/{id}/{get_file_from_path(filename)}")

        if return_data["operationCode"] != 0:
            raise ConnectionError(f"Could not update video file: {return_data}")

        return return_data

    def delete(self, id: str, username: str = None, oauth: bool = False):
        if not username:
            username = self.username

        del_resp = requests.delete(f"{self.url}video/{username}/delete/{id}", headers=self.get_header(oauth))

        if self.json:
            return del_resp.json()
        else:
            return del_resp

    def get_user_videos(self, username: str = None):
        return self.get_request(api_url=f"video/{username}/list")

    def get_video(self, id: str):
        return self.get_request(api_url=f"video/origin/versions/{id}")
