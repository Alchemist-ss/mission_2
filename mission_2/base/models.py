from flask_login import UserMixin
from base import db, manager
from start import composition


# Создание таблицы пользователей
class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Show (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128))

kk = Show(type = composition)
db.session.add(kk)
db.session.commit()

# Логин менеджер для загрузки пользователей
@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
