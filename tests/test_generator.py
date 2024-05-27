import unittest
from generator import passwd_generator




class TestPasswdGenerator(unittest.TestCase):
    
    def test_default_passwd_len(self):
        passwd = passwd_generator()
        self.assertEqual(len(passwd), 12)
    
    def test_custom_passwd_len(self, ):
        passwd_length = 15
        passwd = passwd_generator(passwd_length)
        self.assertEqual(len(passwd), 15)
    
    def test_negative_passwd_len(self, ):
        passwd_length = -12
        passwd = passwd_generator(passwd_length)
        self.assertEqual(len(passwd), 12)

if __name__=="__main__":
    unittest.main()