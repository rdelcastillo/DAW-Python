from __future__ import annotations
from typeguard import typechecked

MAX_HEALTH = 100


@typechecked
class Weapon:

    def __init__(self, name: str, damage: int, durability: int):
        if name == "":
            raise ValueError("El nombre no puede estar vacío")
        if damage <= 0:
            raise ValueError("El daño base tiene que ser mayor que 0")
        if durability <= 0:
            raise ValueError("La durabilidad tiene que ser mayor que 0")

        self.__name = name
        self.__damage = damage
        self.__durability = durability

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        if self.__durability == 0:
            return 0
        return self.__damage

    @property
    def durability(self):
        return self.__durability

    def use(self):
        damage = self.damage
        if self.__durability > 0:
            self.__durability -= 1
        return damage

    def __str__(self):
        return f"Arma: {self.name}, daño base: {self.damage}, durabilidad: {self.durability}"

class Warrior:

    def __init__(self, name: str, health: int, weapon: Weapon):
        if name == "":
            raise ValueError("El nombre no puede estar vacío")
        if health <= 0 or health > MAX_HEALTH:
            raise ValueError(f"La vida tiene que ser mayor que 0 y menor o igual que {MAX_HEALTH}")

        self.__name = name
        self.__health = health
        self.__weapon = weapon

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, value: Weapon):
        self.__weapon = value

    def __str__(self):
        return f"Guerrero: {self.__name} - Vida: {self.__health} - Arma: {self.__weapon.name}"

    def __eq__(self, other: Warrior):
        return self.__name == other.__name

    def __ne__(self, other: Warrior):
        return not (self == other)

    def cure(self, health: int):
        if self.__health <= 0:
            raise ValueError("La vida tiene que ser mayor que 0")
        self.__health = min(self.__health + health, MAX_HEALTH)

    def attack(self, other: Warrior):
        if self.__health <= 0:
            raise ValueError("No se puede atacar si la vida no es mayor que 0")
        damage = self.__weapon.use()
        other.__health = max(0, other.__health - damage)

    @staticmethod
    def duel(g1: Warrior, g2: Warrior):
        while True:
            if g1.weapon.durability == 0 and g2.weapon.durability == 0:
                return "EMPATE"
            g1.attack(g2)
            if g2.health == 0:
                return g1.name
            g2.attack(g1)
            if g1.health == 0:
                return g2.name
