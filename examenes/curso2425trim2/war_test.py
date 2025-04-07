from war import Weapon, Warrior

# Probamos Weapon
sword = Weapon("Espada de Fuego", 25, 3)
sword.use()
print(sword)

# Probamos Warrior
g1 = Warrior("Ragnar", 80, sword)
g2 = Warrior("Lagertha", 100, Weapon("Hacha", 20, 5))
g1.attack(g2)
print(g1)
print(g2)

# Pelea Lagherta contra Ragnar
print(f"Duelo entre [{g2}] y [{g1}]: {Warrior.duel(g2, g1)}")
print(g1)
print(g2)