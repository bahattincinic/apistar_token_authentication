from apistar.parsers import JSONParser

settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sql',
        }
    },
    'INSTALLED_APPS': (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'example',
    ),
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
        'ORM': 'django',
        'USER_MODEL': 'User',
        'TOKEN_MODEL': 'AccessToken'
    }
}
