from apistar import Settings
from apistar.exceptions import ConfigurationError

from .utils import import_from_string


SETTINGS_KEY = 'TOKEN_AUTHENTICATION'

DEFAULTS = {
    'IS_EXPIRY_TOKEN': False,
    'EXPIRY_TIME': 30,
    'USERNAME_FIELD': 'username',
    'PASSWORD_FIELD': 'password',
    'ORM': 'sqlalcamy',
    'ENCRYPTION_FUNCTION': lambda x: x
}

IMPORT_STRINGS = (
    'USER_MODEL',
    'TOKEN_MODEL',
    'ENCRYPTION_FUNCTION'
)


def get_settings(settings: Settings):
    user_settings = dict(DEFAULTS)
    user_settings.update(settings.get(SETTINGS_KEY, {}))

    for module in IMPORT_STRINGS:
        if module not in user_settings and module not in DEFAULTS:
            raise ConfigurationError(f'{module} settings is required.')

        if user_settings['ORM'] == 'sqlalcamy':
            user_settings[module] = import_from_string(user_settings[module])

    return user_settings
