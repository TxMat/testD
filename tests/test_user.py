from datetime import date
import unittest
from src.model.experience import Experience
from src.model.user import User

class TestUser(unittest.TestCase):
    user = None
    def setUp(self) -> None:
        self.user_name = "Jhon"
        self.user_lastname = "Doe"
        self.user_email = "JohnDoe@example.com"
        self.user_password = "NotSoStrongPWD1234!"
        self.user_birthday = date(1998, 4, 10)
        self.user = User(
            self.user_name,
            self.user_lastname, 
            self.user_email, 
            self.user_password, 
            self.user_birthday)
        print("setup")   
    def test_update_password(self) -> None:
        bad_pwd = [
            "aA123!",               # password to short
            "aAAAAAAAAAAAA123",     # missing special
            "aAAAAAAAAAAAA!",       # missing numeric
            "aaaaaaaaaaa123!",      # missing uppercase
            "AAAAAAAAAA123!",       # missing lowercase
            "aaaaaaaaaaa123!",       # missing upercase
            "aaaaaaaaaaaaaaaaa123!aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" , # password to long

        ]
        for pwd in bad_pwd:
            self.assertRaises(AttributeError, self.user.update_password, pwd)

if __name__ == '__main__':
    unittest.main()