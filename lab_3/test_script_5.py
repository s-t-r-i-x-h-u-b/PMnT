import unittest
import script_5

class TestAuthManager(unittest.TestCase):
    def setUp(self):
        self.auth = script_5.AuthManager()
    
    def test_valid_age_positive_number(self):
        self.assertTrue(self.auth.valid_age(25))
    
    def test_valid_age_min_boundary(self):
        self.assertTrue(self.auth.valid_age(0))
    
    def test_valid_age_max_boundary(self):
        self.assertTrue(self.auth.valid_age(150))
    
    def test_valid_age_negative_number(self):
        self.assertFalse(self.auth.valid_age(-1))
    
    def test_valid_age_above_max(self):
        self.assertFalse(self.auth.valid_age(200))


if __name__ == '__main__':
    unittest.main()
