from selenium import webdriver

from urllib.parse import unquote
import requests
import json


def get_token(username: str = None, password: str = None, client_id: str = None, client_key: str = None):
    session = requests.Session()

    """
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    """

    driver = webdriver.Firefox()
    driver.get(
        f"https://eduplay.rnp.br/portal/oauth/authorize?response_type=code&client_id={client_id}&scope=ws:write&redirect_uri=https://localhost:4443"  # noqa: E501
    )

    while "https://localhost:4443/?code=" not in driver.current_url:
        pass

    code = driver.current_url[29:]
    driver.close()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    token_data = {
        "code": unquote(code),
        "client_id": client_id,
        "redirect_uri": "https://localhost:4443",
        "grant_type": "authorization_code",
        "client_secret": client_key,
    }

    token_post = session.post(
        "https://eduplay.rnp.br/portal/oauth/token",
        headers=headers,
        data=token_data,
    )

    return json.loads(token_post.content)["access_token"]
