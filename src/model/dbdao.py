import sqlite3
import pickle
#Temporary for testing purposes
from src.model.user_exception import * 
SAVE_PATH = "data/serialized_user.pickle"
from src.model.user import User 

class DbDao(): 
    def __init__(self): 
        self
    
    def save_user(self, user : User) -> None:
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