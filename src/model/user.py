from datetime import date
from dateutil.relativedelta import relativedelta
from .experience import Experience
import hashlib
from email_validator import validate_email, EmailNotValidError
from geopy.geocoders import Nominatim

def get_hash(input_str : str) -> str:
    return hashlib.sha256(input_str.encode()).hexdigest()

def format_naming_input(input_str : str) -> str:
    """Return formated name or last name :
        Remove whitespace
        raise ValueError if input_str contains non alphanumeric different from '-'
    Args:
        input_str (str): name or lastname to format

    Raises:
        ValueError: [description]

    Returns:
        str: name or lastname formated
    """
    if (any(not char.isalnum() and char != '-'  for char in input_str)):
        raise ValueError
    return input_str.replace(" ", "")

class User:
    
    def __init__(self, id : int, name : str, lastname : str, email : str, password : str, birthday : date ):
        """Create a standard user object

        Args:
            id (int): [description]
            name (str): [description]
            lastname (str): [description]
            email (str): [description]
            password (str): [description]
            birthday (date): [description]
        """
        print("AAAAA" + password)
        self._id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.update_password(password)
        self.__location = None
        age = relativedelta(date.today(), birthday).years
        if age < 15:
            raise ValueError("l'age requis n'est pas atteint ({} < 15)".format(age))
        else :
            self.__birthday = birthday
        
    
    
    def update_password(self, password : str) -> None:
        """Update the user password hash 
        raise ValueError if password to weak
        length should be between 8 and 36 chars
        use at least 1 numeric 
        use at least 1 special char
        use at least 1 uppercase and 1 small caps
        Args:
            password (str): Password string
        """
        print( password)
        special = "?.;:!@#$^\{\}\\/<>+-=&~'()[]-|`_@€µ%"
        if (
            len(password) < 8 or len(password) > 36 or 
            not any(char.isdigit() for char in password) or
            not any(char in special for char in password) or
            password.upper() == password or
            password.lower() == password):
            print("Check")
           
            raise ValueError
        self.__password_hash = get_hash(password)

    def is_password_matching(self, password : str) -> bool:
        return get_hash(password) == self.__password_hash
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name : str) -> None:
        """setter name
        throw ValueError if name contains non alpha numeric character (different than '-')

        Args:
            name (str): [description]
        """
        try:
            self.__name = format_naming_input(name)
        except ValueError:
            raise ValueError("format du prénom incorrect")
            
    @property
    def lastname(self) -> str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname : str) -> None:
        """setter lastname
        throw ValueError if lastname contains non alpha numeric character (different than '-')

        Args:
            name (str): [description]
        """
        try:
            self.__lastname = format_naming_input(lastname)
        except ValueError:
            raise ValueError("format du nom incorrect")
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email : str) -> None:
        """Email property setter
            try to set email property by formating
            raise ValueError if email not valid
        Args:
            email (str): 
        """
        try:
            valid = validate_email(email)
            self.__email = valid.email
        except EmailNotValidError:
            raise ValueError("adresse mail incorrecte")
    
    
    @property
    def birthday(self) -> date:
        return self.__birthday
    
    @property
    def age(self) -> int : 
        """Return age in int by calculating it dynamically

        Returns:
            int: [description]
        """
        return relativedelta(self.birthday, date.today()).years
    
    
    
    
    @property
    def address(self) -> str:
        """Return none if location is not set for this user

        Returns:
            str: [description]
        """
        if self.__location is None:
            return None
        else:
            return self.__location.address
    
    @address.setter
    def address(self, address : str) -> None:
        """Set location from an address string
        if the location of the address is not found ValueError is raised

        Args:
            address (str): [description]

        Raises:
            ValueError: [description]
        """
        geolocator = Nominatim(user_agent="default")
        location = geolocator.geocode(address)
        if location is None:
            raise ValueError("l'adresse est incorrecte")
        else:
            self.__location = location
    
    