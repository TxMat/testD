from src.model.feedback import UserCreationFeedback

class UserException(Exception):
    def __init__(self, *args):
        self.Exception = Exception(self, *args, )
        
class UserNotFound(UserException):
    def __init__(self, *args):
        self.UserException = UserException(self, *args, )

class UserAlreadyExists(UserException):
    def __init__(self, *args):
        self.UserException = UserException(self, *args, )

class IncorrectPassword(UserException):
    def __init__(self, *args):
        self.UserException = UserException(self, *args, )
        
class UserCreationException(UserException): 
    def __init__(self, *args, feedback=[] ):
        self.UserException = UserException(self, *args, )
        self.__feedback = feedback
    
    @property
    def feedback(self) -> list['UserCreationFeedback']:
        return self.__feedback