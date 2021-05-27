from pyrnp import RNP

import responses
import unittest


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PublishTestCase))
    return suite


class PublishTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", username="niki")

    @responses.activate
    def test_can_publish(self):
        responses.add(responses.POST, "https://eduplay.rnp.br/services/video/niki/save/video_unique_id/video.mp4")
        response = self.client.publish(
            filename="video.mp4", id="video_unique_id", title="title", keywords="test upload", thumbnail="thumb.png"
        )

        self.assertIn(
            b'{"title": "title", "keywords": "test upload", "thumbnail": "thumb.png"}', response.request.body
        )

    def test_requires_title(self):
        with self.assertRaisesRegex(ValueError, "'title' must be set"):
            self.client.publish()

    def test_requires_keywords(self):
        with self.assertRaisesRegex(ValueError, "'keywords' must be set"):
            self.client.publish(title="title")

    def test_requires_filename(self):
        with self.assertRaisesRegex(ValueError, "'filename' must be set"):
            self.client.publish(title="title", keywords="keywords")

    def test_requires_id(self):
        with self.assertRaisesRegex(ValueError, "'id' must be set"):
            self.client.publish(title="title", keywords="keywords", filename="video.mp4")


if __name__ == "__main__":
    unittest.main()
