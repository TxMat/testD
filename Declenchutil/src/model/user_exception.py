class UserException(Exception):
    def __init__(self, *args, **kwargs):
        self.Exception = Exception(self, *args, **kwargs)
        
class UserNotFound(UserException):
    def __init__(self, *args, **kwargs):
        self.UserException = UserException(self, *args, **kwargs)

class UserAlreadyExists(UserException):
    def __init__(self, *args, **kwargs):
        self.UserException = UserException(self, *args, **kwargs)

class IncorrectPassword(UserException):
    def __init__(self, *args, **kwargs):
        self.UserException = UserException(self, *args, **kwargs)