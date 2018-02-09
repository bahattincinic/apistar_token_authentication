# SQLAlchemy Setup

Add Access Token model in your project.

```python
from django.db import models
from typing import Any

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

Base: Any = declarative_base()

class AccessToken(Base):
    __tablename__ = 'access_tokens'

    id = Column(Integer, primary_key=True)
    token = Column(String)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer)

```

Add configuration settings

```python
{
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
```

Access user instance from Handlers

```python
from apistar import annotate
from apistar.backends.django_orm import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated
from apistar_token_auth.authentication import SQLAlchemyTokenAuthentication


@annotate(authentication=[SQLAlchemyTokenAuthentication()],
          permissions=[IsAuthenticated()])
def user_profile(session: Session, auth: Auth):
    return {
        'username': auth.user.username
    }

```
