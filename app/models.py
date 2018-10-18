from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Repository(db.Model):
    __tablename__ = 'repository'
    id = db.Column(db.Integer,primary_key = True)
    row = db.Column(db.Integer)
    column = db.Column(db.Integer)
    type = db.Column(db.String(64))
    products = db.relationship('Product', backref='rpo', lazy='dynamic')
    product_id = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<Repository %r>' % self.id


class Product(db.Model):
    __tablename__='product'
    id = db.Column(db.Integer,primary_key = True)
    order_id = db.Column(db.Integer)
    type = db.Column(db.String(64))
    status = db.Column(db.String(64))
    position = db.Column(db.String(64))
    rpo_id = db.Column(db.Integer, db.ForeignKey('repository.id'))

    def __repr__(self):
        return '<Product %r>' % self.id

class Equipment(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    ept_name = db.Column(db.String(64), unique=True, index=True)
    status = db.Column(db.String(64))
    position = db.Column(db.String(64))
