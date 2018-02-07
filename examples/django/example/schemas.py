from apistar import typesystem


class Password(typesystem.String):
    description = 'Password'


class Username(typesystem.String):
    description = 'Username'


class SignupData(typesystem.Object):
    properties = {
        'username': Username,
        'password': Password
    }
    required = ['username', 'password']
