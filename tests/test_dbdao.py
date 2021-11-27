import os
from datetime import date
import unittest

from src.model.user import User
from src.model.dbdao import DbDao
from src.model.user_exception import *

password = "NotSoStrongPWD1234!"
birthday = date(1998, 4, 10)
id = 1
class TestDbDao(unittest.TestCase):
    
    def setUp(self) -> None:
        self.dao = DbDao()
        self.user_manipulated = User(id, "Roger", "Martin", "roger@gmail.com", password,birthday )
        try:
            os.remove("data/serialized_user.pickle")
        except FileNotFoundError:
            pass
    def test_save_load_user(self):
        self.dao.save_user(self.user_manipulated)
        user = self.dao.load_user(self.user_manipulated.email)
        self.assertEqual(user, self.user_manipulated)
        with self.assertRaises(UserNotFound):
            self.dao.load_user("julien@outlook.fr")
        
        with self.assertRaises(UserAlreadyExists):
            self.dao.save_user(self.user_manipulated)
    
    def test_remove_user(self):
        try:
            self.dao.save_user(self.user_manipulated)
        except UserAlreadyExists:
            pass
        self.dao.remove_user(self.user_manipulated.id)
        with self.assertRaises(UserNotFound):
            self.dao.remove_user(self.user_manipulated.id)
    
    def test_get_user_id(self):
        try:
            self.dao.save_user(self.user_manipulated)
        except UserAlreadyExists:
            pass
        self.assertEqual(id+1, self.dao.get_new_user_id())
            
    
if __name__ == '__main__':
    unittest.main()