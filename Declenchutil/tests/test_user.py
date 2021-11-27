from datetime import date
import unittest
from src.model.user import User

name = "Jhon"
lastname = "Doe"
email = "JohnDoe@example.com"
password = "NotSoStrongPWD1234!"
password2 = "Ver235yStro#ngPWD"
birthday = date(1998, 4, 10)
id = 1
class TestUser(unittest.TestCase):
    user = None
    
    def setUp(self) -> None:
        self.user = User(
            id,
            name,
            lastname, 
            email, 
            password, 
            birthday)
        
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
            self.assertRaises(ValueError, self.user.update_password, pwd)
        self.user.update_password(password2)

    def test_password_matching(self) -> None:
        self.user.update_password(password2)
        self.assertTrue(self.user.is_password_matching(password2))
        self.assertTrue(not self.user.is_password_matching(password))

    def test_name_lastname_format(self) -> None:
        invalid_name = "###''))"
        with self.assertRaises(ValueError):
            self.user.lastname = invalid_name
    
    def test_address(self) -> None :
        valid_address = "25 Rue Casimir Brenier Grenoble 38000"
        invalid_address = "25 Rue Casimir Brenier Paris 45000"
        self.user.address = valid_address # No exception should be raised
        with self.assertRaises(ValueError):
            self.user.address = invalid_address
    
    def test_equality(self) -> None:
        user_equal = User(
            id,
            name,
            lastname, 
            email, 
            password, 
            birthday)
        
        user_not_equal = User(
            id + 3,
            name + "New",
            lastname, 
            email, 
            password, 
            birthday)
        
        self.assertEqual(user_equal, self.user)
        self.assertNotEqual(user_not_equal, self.user)
        
"""
class TestClientUser(unittest.TestCase):
    user = None
    def setUp(self) -> None:
        self.user = ClientUser()
"""     
    
if __name__ == '__main__':
    unittest.main()