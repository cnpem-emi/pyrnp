from pyrnp import RNP

import responses
import unittest


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DeleteTestCase))
    return suite


class DeleteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY")

    @responses.activate
    def test_can_delete(self):
        responses.add(responses.DELETE, "https://eduplay.rnp.br/services/video/niki/delete/video_id")
        self.client.delete(id="video_id", username="niki")

    def test_requires_id(self):
        with self.assertRaisesRegexp(ValueError, "'id' must be set"):
            self.client.delete()


if __name__ == "__main__":
    unittest.main()
