from enum import Enum
class UserCreationFeedback(Enum):
    NAME_ERROR = 'Le prénom ne peut pas contenir de chiffres / caractères spéciaux (hormis /)'
    LASTNAME_ERROR = 'Le nom ne peut pas contenir de chiffres / caractères spéciaux (hormis /)'
    EMAIL_ERROR = "L'adresse email est incorrecte"
    PASSWORD_ERROR = """Un mot de passe doit :
    - comprendre entre 8 et 36 caractères
    - contenir 1 chiffres
    - contenir 1 caractère spécial (#/!? ...)
    - contenir 1 majuscule et 1 minuscule"""
    BIRTHDAY_ERROR = "Vous devez avoir plus de 15 ans pour vous inscrire"