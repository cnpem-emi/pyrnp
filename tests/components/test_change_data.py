from pyrnp import RNP

import responses
import unittest


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ChangeDataTestCase))
    return suite


class ChangeDataTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", username="niki")

    @responses.activate
    def test_can_delete(self):
        responses.add(responses.POST, "https://eduplay.rnp.br/services/video/niki/update/1990?changeAssociation=false")
        self.client.change_data(id="1990", title="Video Title", keywords="Keywords")

    def test_requires_id(self):
        with self.assertRaisesRegexp(ValueError, "'id' must be set"):
            self.client.change_data()

    def test_requires_title(self):
        with self.assertRaisesRegexp(ValueError, "'title' must be set"):
            self.client.change_data(id="1991")

    def test_requires_keywords(self):
        with self.assertRaisesRegexp(ValueError, "'keywords' must be set"):
            self.client.change_data(id="1992", title="Video Title")


if __name__ == "__main__":
    unittest.main()
