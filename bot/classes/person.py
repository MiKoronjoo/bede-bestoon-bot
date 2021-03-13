from pymongo.collection import Collection

from .dept import Dept
from .entity import Entity
from .user import User


class Person(Entity):
    def __init__(self, object_id, name, username=None):
        self.id = object_id
        self.name = name
        self.username = username

    @staticmethod
    def table() -> Collection:
        return Person.db().person

    @property
    def user(self):
        user_id = Person.table().find_one({'_id': self.id}).user
        return User.get_user(user_id)

    @property
    def depts(self):
        return [Dept(dept['_id'], dept.amount, dept.type, dept.detail)
                for dept in Dept.table().find({'person': self.id})]

    @staticmethod
    def get_person(person_id):
        person = Person.table().find_one({'_id': person_id})
        return Person(person_id, person.name, person.username)
