from apistar import Response, annotate
from apistar.backends.django_orm import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated

from apistar_token_auth.authentication import DjangoTokenAuthentication
from .schemas import SignupData


@annotate(authentication=[DjangoTokenAuthentication()],
          permissions=[IsAuthenticated()])
def user_profile(session: Session, auth: Auth):
    return {
        'username': auth.user.username
    }


def signup(session: Session, data: SignupData):
    user = session.User(
        username=data['username']
    )
    user.set_password(data['password'])
    user.save()

    return {
        'id': user.id,
        'username': user.username
    }
