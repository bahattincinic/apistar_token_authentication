
from apistar.frameworks.asyncio import ASyncIOApp as App
from apistar.backends import sqlalchemy_backend

from example.routes import routes
from example.settings import settings


app = App(
    routes=routes,
    settings=settings,
    components=sqlalchemy_backend.components,
    commands=sqlalchemy_backend.commands
)

if __name__ == '__main__':
    app.main()
