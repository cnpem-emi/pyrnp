import json
import unittest

from pyrnp import RNP
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetUserVideosTestCase))
    return suite


class GetUserVideosTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", json=False)

    @responses.activate
    def test_can_get_user_videos(self):
        responses.add(responses.GET, "https://eduplay.rnp.br/services/video/niki/list")
        self.client.get_user_videos(username="niki")


if __name__ == "__main__":
    unittest.main()
