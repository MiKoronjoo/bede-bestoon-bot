from pymongo.collection import Collection

from .entity import Entity
from .person import Person
from .dept import Dept


class Language:
    EN = 'EN'
    FA = 'FA'


class User(Entity):
    def __init__(self, user_id, name, language=Language.EN, state=0):
        self.id = str(user_id)
        self.name = name
        self._state = state
        self.language = language

    @staticmethod
    def table() -> Collection:
        return User.db().user

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        User.table().update_one({'id': self.id}, {'state', value})
        self._state = value

    @property
    def balance(self):
        blnc = 0
        for dept in Dept.table().find({'id': self.id}):
            coeff = 1 if dept.type == 0 else -1
            blnc += coeff * dept.amount
        return blnc

    @property
    def persons(self):
        return [Person(person['_id'], person.name, person.username)
                for person in Person.table().find({'user': self.id})]

    @property
    def depts(self):
        return [Dept(dept['_id'], dept.amount, dept.type, dept.detail)
                for dept in Dept.table().find({'user': self.id})]

    @staticmethod
    def get_user(user_id, name=None):
        user = User.table().find_one({'id': str(user_id)})
        if not user:
            User.table().insert_one({'id': str(user_id), 'name': name, 'language': Language.EN, 'state': 0})
            return User(user_id, name)
        return User(user_id, user.name, user.language, user.state)

    def add_person(self, name: str, username: str = None):
        return Person.table().insert_one(dict(name=name, username=username, user=self.id)).inserted_id

    def add_dept(self, person: Person, amount: int, type: int, detail: str = None):
        return Dept.table().insert_one(
            dict(amount=amount, type=type, detail=detail, user=self.id, person=person.id)).inserted_id
