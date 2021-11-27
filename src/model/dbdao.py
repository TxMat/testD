import sqlite3
import pickle #Temporary for testing purposes
from src.model.user_exception import * 
import os
from src.model.user import User 

SAVE_PATH = "data"
if not os.path.isdir(SAVE_PATH):
    SAVE_PATH = "Declenchutil/data"
    if not os.path.exists(SAVE_PATH):
        SAVE_PATH = "../data"
SAVE_PATH += "/serialized_user.pickle"

class DbDao: 
    def __init__(self): 
        self
    
    def save_user(self, user : User) -> None:
        """Save the user to the database

        Args:
            user (User): user instance

        Raises:
            UserAlreadyExists: user already exists in the database
        """
        user_list = []
        try:
            self.load_user(user.email)
            raise UserAlreadyExists
        except UserNotFound:
            pass
        
        try:
            with open(SAVE_PATH, "rb") as file:
                user_list = pickle.loads(file)
                
        except Exception:
            user_list = []
        
        with open(SAVE_PATH, "wb") as file:
            user_list.append(user)
            pickle.dump(user_list, file)
    
    def load_user(self, email : str) -> User:
        """get user from database filtered by his id

        Args:
            email (str): email of the user 

        Raises:
            UserNotFound: the user does not exist in the database

        Returns:
            User: user with email == email
        """
        user_list = []
        try:
            with open(SAVE_PATH, "rb") as file:
                user_list = pickle.load(file)
        except FileNotFoundError:
            raise UserNotFound
        found_email = ""
        i = 0
        user = None
        while found_email != email and i < len(user_list):
            user = user_list[i]
            i += 1
            found_email = user.email
        if user is None or found_email != email:
            raise UserNotFound
        else:
            return user
    
    def remove_user(self, id : int) -> None:
        """remove user from database

        Args:
            id (int): id of the user wanted to remove

        Raises:
            UserNotFound: the user is not in the database
        """
        user_list = []
        try:
            with open(SAVE_PATH, "rb") as file:
                user_list = pickle.load(file)
        except FileNotFoundError:
            raise UserNotFound
        found_id = ""
        i = 0
        user = None
        while found_id != id and i < len(user_list):
            user = user_list[i]
            i += 1
            found_id = user.id
        if found_id != id:
            raise UserNotFound
        else:
            del user_list[i-1]
            with open(SAVE_PATH, "wb") as file:
                pickle.dump(user_list, file)
    
    def get_new_user_id(self) -> int:
        """Return an id that is free from user

        Returns:
            int: [description]
        """
        user_list = []
        try:
            with open(SAVE_PATH, "rb") as file:
                user_list = pickle.load(file)
        except FileNotFoundError:
            return 1
        
        max = 1
        for user in user_list:
            if user.id > max:
                max = user.id
        return max + 1