
import unittest
from key_manager import KeyManager

class KeyImportTestCase(unittest.TestCase):
    
    def validate_key(self):
        """ Test key is non-empty string"""
        self.key_manager = KeyManager('test_key.txt')
        key = self.key_manager.get_key()
        self.assertIsNotNone(key)
        self.assertTrue(type(key) == str)

if __name__ == '__main__':
    unittest.main()