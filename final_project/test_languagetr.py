import unittest
from. import languagetr #import en2fr, fr2en
class Testen2fr(unittest.TestCase):
    def test1(self):
        self.assertEqual(languagetr.en2fr('Hello'),"Bonjour")
        self.assertNotEqual(languagetr.en2fr('hello'), "hello")
class Testfr2en(unittest.TestCase):
    def test1(self):
        self.assertEqual(languagetr.fr2en('Bonjour'),"hello")
        self.assertNotEqual(languagetr.fr2en('Bonjour'), "Namaste")
# unittest.main()