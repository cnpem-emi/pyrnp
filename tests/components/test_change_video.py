from pyrnp import RNP

import responses
import unittest


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ChangeVideoTestCase))
    return suite


class ChangeVideoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", username="niki")

    @responses.activate
    def test_can_change_video(self):
        responses.add(
            responses.POST, "https://eduplay.rnp.br/services/video/niki/change/file/default/video_unique_id/video.mp4"
        )
        self.client.change_video(id="video_unique_id", filename="video.mp4")

    def test_requires_id(self):
        with self.assertRaisesRegex(ValueError, "'id' must be set"):
            self.client.change_video(filename="video.mp4")

    def test_requires_filename(self):
        with self.assertRaisesRegex(ValueError, "'filename' must be set"):
            self.client.change_video()


if __name__ == "__main__":
    unittest.main()
