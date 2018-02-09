# Configuration

- `IS_EXPIRY_TOKEN`: if it False, user token will not expire. (default: False)
- `EXPIRY_TIME`: this value is based on days. For example: 30 (default: 30)
- `USERNAME_FIELD`: the user identifier is the username, it uses for custom user models. (default: username)
- `PASSWORD_FIELD`: it uses for custom user models. (default: password)
- `ORM`: it should be `sqlalcamy` or `django`
- `USER_MODEL`:
    - it should be model path for sqlalcamy. (for example: example.models.User)
    - it should be model name for Django (for example: User)
- `TOKEN_MODEL`:
    - it should be model path for sqlalcamy. (for example: example.models.User)
    - it should be model name for Django (for example: User)
- `ENCRYPTION_FUNCTION`: it should be function path. (for example: example.utils.hash_password) this field only required for sqlalcamy.