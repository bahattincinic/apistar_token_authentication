# Django Setup

Add Access Token model in your project.

```python
from django.db import models


class AccessToken(models.Model):
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```

Add configuration settings

```python
{
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
```

Access user instance from Handlers

```python
from apistar import annotate
from apistar.backends.django_orm import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from apistar_token_auth.authentication import DjangoTokenAuthentication


@annotate(authentication=[DjangoTokenAuthentication()],
          permissions=[IsAuthenticated()])
def user_profile(session: Session, auth: Auth):
    return {
        'username': auth.user.username
    }

```
