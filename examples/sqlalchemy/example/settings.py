from apistar.parsers import JSONParser

from .models import Base


settings = {
    'DATABASE': {
        'URL': 'sqlite:///db.sql',
        'METADATA': Base.metadata
    },
    'PARSERS': [JSONParser()],
    'SCHEMA': {
        'TITLE': 'example',
        'DESCRIPTION': 'example App'
    },
    'TOKEN_AUTHENTICATION': {
        'IS_EXPIRY_TOKEN': True,
        'EXPIRY_TIME': 30,
        'USERNAME_FIELD': 'username',
        'PASSWORD_FIELD': 'password',
        'ORM': 'sqlalcamy',
        'USER_MODEL': 'example.models.User',
        'TOKEN_MODEL': 'example.models.AccessToken',
        'ENCRYPTION_FUNCTION': 'example.utils.hash_password'
    }
}
