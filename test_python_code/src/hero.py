from typing import List
import functools

def log(func):
    @functools.wraps()
    def wrapper(*args, **kargs):
        print(func.__name__)
        return func(*args, **kargs)
    return wrapper


class Hero:
    hp = 100
    power: int = 10
    magic_hp = 200
    speed = 100
    tools = []
    name = ""

    def fight(self, hero: 'Hero'):
        while True:
            if self.speed < hero.speed:
                hero.hp -= self.power
                if self.winner(self, hero):
                    return True
            else:
                self.hp -= hero.power
                if self.winner(hero, self):
                    return False

    @log
    def winner(self, hero1, hero2):
        print(f"{hero1} VS {hero2}")
        if hero1.hp <= 0:
            print("False")
            return False
        elif hero2.hp <= 0:
            print("True")
            return True

    def fight_many(self, heros: List['Hero']):
        pass

