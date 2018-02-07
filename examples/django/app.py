
from apistar.frameworks.asyncio import ASyncIOApp as App
from apistar.backends import django_orm

from example.routes import routes
from settings import settings


app = App(
    routes=routes,
    settings=settings,
    components=django_orm.components,
    commands=django_orm.commands
)

if __name__ == '__main__':
    app.main()
