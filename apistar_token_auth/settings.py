from apistar import Settings
from apistar.exceptions import ConfigurationError

from .utils import import_from_string


SETTINGS_KEY = 'TOKEN_AUTHENTICATION'

DEFAULTS = {
    'IS_EXPIRY_TOKEN': False,
    'EXPIRY_TIME': 30,
    'USERNAME_FIELD': 'username',
    'PASSWORD_FIELD': 'password',
    'ORM': 'sqlalcamy'
}

IMPORT_STRINGS = (
    'USER_MODEL',
    'TOKEN_MODEL',
    'ENCRYPTION_FUNCTION'
)


def get_settings(settings: Settings):
    user_settings = dict(settings.get(SETTINGS_KEY, {}))
    user_settings.update(DEFAULTS)

    for module in import_from_string:
        if module not in settings:
            raise ConfigurationError(f'{module} settings is required.')

        if user_settings['ORM'] == 'sqlalcamy'
            user_settings[module] = import_from_string(user_settings[module])

    return user_settings
