from pyrnp import RNP

import responses
import unittest


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetVideoTestCase))
    return suite


class GetVideoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY")

    @responses.activate
    def test_can_get_video(self):
        responses.add(responses.GET, "https://eduplay.rnp.br/services/video/origin/versions/video_id")
        self.client.get_video(id="video_id")

    def test_requires_id(self):
        with self.assertRaisesRegexp(ValueError, "'id' must be set"):
            self.client.get_video()


if __name__ == "__main__":
    unittest.main()
