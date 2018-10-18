import os
from app import create_app, db
from app.models import User, Role,Repository,Product
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User,Role=Role,Repository=Repository)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#创建数据库
@manager.command
def create():
    db.drop_all()
    db.create_all()
    #初始仓库建立
    for row in range(1,5):
        for column in range(1,5):
            rpo = Repository(row=row,column=column,type='空')
            db.session.add(rpo)
            print(row)
            print(column)
    for i in range(20):
        product = Product(order_id=1002,type='成品',status='成品',position='已出库')
        db.session.add(product)






manager.add_command("shell", Shell(make_context=make_shell_context()))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()