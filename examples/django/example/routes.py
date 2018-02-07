from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls
from apistar_token_auth.handlers import django_get_token

from example.views import user_profile, signup


routes = [
    Route('/', 'GET', user_profile, 'User-Profile'),
    Route('/signup', 'POST', signup, 'Signup'),
    Route('/token', 'POST', django_get_token, 'Login'),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
