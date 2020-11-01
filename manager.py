import os

# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from apps import create_app
# from apps import db

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
manager = Manager(app)
# migrate = Migrate(app, db)


def make_shell_context():
    return {
        'app': app,
        # 'db': db,
    }


manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
