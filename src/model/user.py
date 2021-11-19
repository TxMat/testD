from datetime import date
from .experience import Experience
import hashlib

class User:
    __name = ""
    __lastname = ""
    __email = ""
    __password_hash = ""
    __birthday = ""
    def __init__(self, name : str, lastname : str, email : str, password : str, birthday : date ):
        """constructor

        Args:
            name (str): name of the user
            lastname (str): lastname of the user
            email (str): email of the user
            password (str): password of the user
            birthday (date): date of birth of the user
            

        Returns:
            User: new created user
        """
        self.name = name
        self.lastname = lastname
        self.email = email
        self.update_password(password)
        self.birthday = birthday
        
    
    def update_password(self, password : str) -> None:
        """Update the user password hash 
        raise AttributeError if password to weak
        length should be between 8 and 36 chars
        use at least 1 numeric 
        use at least 1 special char
        use at least 1 uppercase and 1 small caps
        Args:
            password (str): Password string
        """
        special = "?.;:!@#$^\{\}\\/<>+-=&~'()[]-|`_@€µ%"
        if (
            len(password) < 8 or len(password) > 36 or 
            not any(char.isdigit() for char in password) or
            not any(char in special for char in password) or
            password.upper() == password or
            password.lower() == password):
            raise AttributeError
        self.__password_hash = hashlib.sha256(password.encode()).hexdigest()

