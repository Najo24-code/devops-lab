import unittest

from app.main import hello


class TestHello(unittest.TestCase):

    def test_hello_returns_expected_message(self):
        self.assertEqual(hello(), "Hello DevOps!")


if __name__ == "__main__":
    unittest.main()
