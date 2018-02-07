from apistar import Settings
from apistar.exceptions import ValidationError

try:
    from apistar.backends.sqlalchemy_backend import Session as SqlalchemySession
except ImportError:
    SqlalchemySession = None

try:
    from apistar.backends.django_orm import Session as DjangoSession
except ImportError:
    DjangoSession = None

from .schemas import Login
from .settings import get_settings
from .utils import generate_key


def django_get_token(session: DjangoSession, settings: Settings,
                     data: Login):
    from django.contrib.auth import authenticate

    user_settings = get_settings(settings)
    user = authenticate(
        username=data['username'],
        password=data['password']
    )

    if not user:
        raise ValidationError(detail='Username or password invalid')
    
    TokenModel = getattr(session, user_settings['TOKEN_MODEL'])
    instance = TokenModel.objects.create(
        user=user, token=generate_key()
    )
    return {'token': instance.token}


def sqlalcamy_get_token(session: SqlalchemySession, settings: Settings,
                        data: Login):
    user_settings = get_settings(settings)
    username = data['username']
    password = user_settings['ENCRYPTION_FUNCTION'](data['password'])

    UserModel = user_settings['USER_MODEL']
    TokenModel = user_settings['TOKEN_MODEL']
    filters = {
        user_settings['USERNAME_FIELD']: username,
        user_settings['PASSWORD_FIELD']: password
    }
    user = session.query(UserModel).filter_by(**filters).first()

    if not user:
        raise ValidationError(detail='Username or password invalid')
    
    token = TokenModel(
        token=generate_key(), user_id=user.id
    )
    session.add(token)

    return {'token': token.token}
