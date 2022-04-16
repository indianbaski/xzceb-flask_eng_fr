import unittestcase

from translator import english_to_french
from translator import french_to_english


class TestString(unittestcase.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test3(self):
        self.assertNotEqual(french_to_english(None), "Hello")

    def test4(self):
        self.assertNotEqual(english_to_french(None), "Bonjour")


unittestcase.main()