import unittest
import translator

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Hello"), "Bonjour")

        
class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()