"""Basic test module for translator module"""
import unittest

from translator import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase):
    """Tests French to English Function"""
    def test1(self):
        """Elementary test function"""
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


class TestEnglishToFrench(unittest.TestCase):
    """Tests English to French Function"""
    def test1(self):
        """Elementary test function"""
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


unittest.main()
