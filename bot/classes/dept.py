from pymongo.collection import Collection

from .entity import Entity
from .person import Person
from .user import User


class Dept(Entity):
    def __init__(self, object_id, amount, type, detail=None):
        self.id = object_id
        self.amount = amount
        self.type = type
        self.detail = detail

    @staticmethod
    def table() -> Collection:
        return Dept.db().dept

    @property
    def user(self):
        user_id = Dept.table().find_one({'_id': self.id}).user
        return User.get_user(user_id)

    @property
    def person(self):
        person_id = Dept.table().find_one({'_id': self.id}).person
        return Person.get_person(person_id)
