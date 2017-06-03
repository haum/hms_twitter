import unittest


class FakeTests(unittest.TestCase):
    def test_trueness(self):
        self.assertEquals(True and True, True)
