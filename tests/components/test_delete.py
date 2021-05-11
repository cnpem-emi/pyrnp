import unittest

from pyrnp import RNP
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DeleteTestCase))
    return suite


class DeleteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", json=False)

    @responses.activate
    def test_can_delete(self):
        responses.add(responses.DELETE, "https://eduplay.rnp.br/services/video/niki/delete/video_id")
        self.client.delete(id="video_id", username="niki")


if __name__ == "__main__":
    unittest.main()
