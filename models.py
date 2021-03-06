from mongoengine import *
from flask.ext.login import UserMixin

MONGO_HOST = ''#Example 'mongodb://user:password@ds031932.mongolab.com:31932/db'
connect(host=MONGO_HOST)

class User(Document):
    login = StringField(required=True, unique=True)
    password = StringField(required=True, max_length=200)

class AuthUser(UserMixin):
    def __init__(self, id):
        users = User.objects(login=id)
        if not users:
            raise UserNotFoundError()
        else:
            self.id = id
            self.password = users.first().password

    @classmethod
    def get(self_class, id):
        try:
            return self_class(id)
        except UserNotFoundError:
            return None

class UserNotFoundError(Exception):
    pass
