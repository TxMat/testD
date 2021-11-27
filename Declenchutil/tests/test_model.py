from datetime import date
import os
import unittest
from src.model.user import User
from src.model.model import Model
from src.model.user_exception import IncorrectPassword, UserAlreadyExists

SAVE_PATH = "data"
if not os.path.isdir(SAVE_PATH):
    SAVE_PATH = "Declenchutil"
SAVE_PATH += "/serialized_user.pickle"

name = "Jhon"
lastname = "Doe"
email = "JohnDoe@example.com"
password = "NotSoStrongPWD1234!"
password2 = "Ver235yStro#ngPWD"
birthday = date(1998, 4, 10)
id = 1

class TestModel(unittest.TestCase):
    user = None
    
    def setUp(self) -> None:
        self.model = Model()
        self.new_user = None
        self.user_reference =  self.user = User(
            id,
            name,
            lastname, 
            email, 
            password, 
            birthday)
        try:
            os.remove(SAVE_PATH)
        except FileNotFoundError:
            pass
            
    
    def test_create_user(self):
        #Should not throw an exception
        self.new_user = self.model.create_user(name,
            lastname, 
            email, 
            password, 
            birthday)
        self.assertEqual(self.user_reference, self.new_user)
        
    def test_load_user(self):
        try:
            self.new_user = self.model.create_user(name,
            lastname, 
            email, 
            password, 
            birthday)
        except UserAlreadyExists:
            pass
        user_loaded = self.model.load_user(email, password)
        self.assertEqual(user_loaded, self.user_reference)
        with self.assertRaises(IncorrectPassword):
            user = self.model.load_user(email, password+"foo")
    
if __name__ == '__main__':
    unittest.main()