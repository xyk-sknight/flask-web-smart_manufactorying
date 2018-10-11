from app import create_app, db
from app.models import User, Role,Repository,Product

num = Product.query.filter(id=1).count()
print(num)