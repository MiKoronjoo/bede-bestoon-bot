from .bot import Bot
from .classes.entity import Entity

if __name__ == '__main__':
    Bot(Entity.db()).run()
