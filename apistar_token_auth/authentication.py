import datetime

from apistar import http, Settings
from apistar.authentication import Authenticated
from apistar.backends.sqlalchemy_backend import Session as SqlalchemySession
from apistar.backends.django_orm import Session as DjangoSession

from .settings import get_settings


class BaseAuthentication():

    def get_credentials(authorization: http.Header):
        if authorization is None:
            return None

        scheme, token = authorization.split()
        if scheme.title() != 'Token' or not token:
            return None

        return token


class SQLAlchemyTokenAuthentication(BaseAuthentication):

    def authenticate(self, authorization: http.Header,
                     session: SqlalchemySession,
                     settings: Settings) -> typing.Union[None, Authenticated]:
        user_settings = get_settings(settings)
        token = self.get_credentials()

        if not token:
            return

        TokenModel = user_settings['TOKEN_MODEL']
        UserModel = user_settings['USER_MODEL']
        instance = session.query(TokenModel).filter(TokenModel.token==token)
        if not instance:
            return
        
        difference = datetime.timedelta(days=user_settings['EXPIRY_TIME'])
        if user_settings['IS_EXPIRY_TOKEN'] and token.created < (now - difference):
            return
        
        user = session.query(UserModel).filter(UserModel.id == instance.user_id)
        return Authenticated(username=getattr(user, user_settings['USERNAME_FIELD']))


class DjangoTokenAuthentication(BaseAuthentication):

    def authenticate(self, authorization: http.Header,
                     session: DjangoSession,
                     settings: Settings) -> typing.Union[None, Authenticated]:
        user_settings = get_settings(settings)
        token = self.get_credentials()

        if not token:
            return
        
        user_settings = get_settings(settings)
        token = self.get_credentials()

        if not token:
            return

        TokenModel = getattr(session, user_settings['TOKEN_MODEL'])
        UserModel = getattr(session, user_settings['USER_MODEL'])
        instance = TokenModel.objects.filter(token=token).first()
        if not instance:
            return

        difference = datetime.timedelta(days=user_settings['EXPIRY_TIME'])
        if user_settings['IS_EXPIRY_TOKEN'] and token.created < (now - difference):
            return

        user = UserModel.objects.filter(id=instance.user_id)
        return Authenticated(username=getattr(user, user_settings['USERNAME_FIELD']))
