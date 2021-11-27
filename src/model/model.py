from datetime import date
from src.model.dbdao import DbDao
from src.model.user import User
from src.model.user_exception import IncorrectPassword, UserNotFound


class Model:
    def __init__(self):
        self.dao = DbDao()
        
    
    def create_user(self,
                    name : str, 
                    lastname : str, 
                    email : str, 
                    password : str, 
                    birthday : date) -> User :
        """Create a new user with info given and saves it to the database
        if the info are incorrect UserCreationException raised with message attribute

        Args:
            name (str): [description]
            lastname (str): [description]
            email (str): [description]
            password (str): [description]
            birthday (date): [description]

        Returns:
            User: [description]
        """
        id = self.dao.get_new_user_id()
        user = User(id, name, lastname, email, password, birthday)
        self.dao.save_user(user)
        return user
    
    def load_user(self, email : str, password : str):
        """Return an user if email and password found
        else raise IncorrectPassword if password is incorrect
        else raise UserNotFound if not found

        Args:
            email (str): [description]
            password (str): [description]

        Raises:
            IncorrectPassword: password does not match
            UserNotFound: user not in the database

        Returns:
            user: user searched for
        """
        
        try:
            user = self.dao.load_user(email)
        except UserNotFound:
            raise UserNotFound
            
        if user.is_password_matching(password):
            return user
        else:
            raise IncorrectPassword
        