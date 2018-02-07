from apistar import Response, annotate
from apistar.backends.sqlalchemy_backend import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated

from apistar_token_auth.authentication import SQLAlchemyTokenAuthentication
from .schemas import SignupData
from .models import User
from .utils import hash_password


@annotate(authentication=[SQLAlchemyTokenAuthentication()],
          permissions=[IsAuthenticated()])
def user_profile(session: Session, auth: Auth):
    return {
        'username': auth.user.username
    }


def signup(session: Session, data: SignupData):
    user = User(
        username=data['username'],
        password=hash_password(data['password'])
    )
    session.add(user)
    session.flush()

    return {
        'id': user.id,
        'username': user.username
    }
