import unittest
from pyrnp import RNP


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RnpClientTestCase))
    return suite


class RnpClientTestCase(unittest.TestCase):
    def test_init_sets_config(self):
        client = RNP(client_id="ID", client_key="KEY")
        self.assertEqual(client.client_id, "ID")
        self.assertEqual(client.client_key, "KEY")

    def test_init_sets_username(self):
        client = RNP(client_id="ID", client_key="KEY", username="russell.george@williams.com")
        self.assertEqual(client.username, "russell.george@williams.com")

    def test_init_sets_token(self):
        client = RNP(client_id="ID", client_key="KEY", token="TOKEN")
        self.assertEqual(client.token, "TOKEN")

    def test_init_sets_oauth(self):
        client = RNP(client_id="ID", client_key="KEY", oauth=True)
        self.assertEqual(client.oauth, True)

    def test_init_sets_platform(self):
        client = RNP(client_id="ID", client_key="KEY", platform="eduplay_test")
        self.assertEqual(client.url, "https://hmg.eduplay.rnp.br/services/")

    def test_invalid_platform_name(self):
        with self.assertRaisesRegex(
            NameError, "Invalid platform selected. Available platforms: eduplay, rnp, rnp_test"
        ):
            RNP(client_id="ID", client_key="KEY", platform="INVALID")

    def test_set_token(self):
        client = RNP(client_id="ID", client_key="KEY")
        client.token = "TOKEN"
        self.assertEqual(client.token, "TOKEN")

    def test_get_header_with_token(self):
        client = RNP(client_id="ID", client_key="KEY", token="TOKEN", oauth=True)
        self.assertEqual(
            client.get_header(),
            {
                "Accept-Encoding": None,
                "clientkey": "KEY",
                "User-Agent": "curl/7.68.0",
                "Authorization": "Bearer TOKEN",
            },
        )


if __name__ == "__main__":
    unittest.main()
