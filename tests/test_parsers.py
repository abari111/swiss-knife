import os
import unittest

from parsers import email_parser

class TestEmailParser(unittest.TestCase):
    def test_extract_emails(self, ):
        file_name = 'assets/text_emails.txt'
        extracted_addrs = email_parser(file_name)
        addrs = []
        self.assertListEqual(extracted_addrs, addrs)
        
    def test_zero_emails(self):
        file_name = 'assets/text_emails.txt'
        extracted_addrs = email_parser(file_name)
        addrs = []
        self.assertListEqual(extracted_addrs, addrs)

if __name__=="__main__":
    unittest.main()