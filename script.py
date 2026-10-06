import math
from tabulate import tabulate

melee_weapons = [["Sword", 5], ["Axe", 7], ["Staff", 3], ["Glaive", 9]]
ranged_weapons = [["Bow", 3], ["Crossbow", 5]]
magic_weapons = [["Wand", 6], ["Magic Staff", 8], ["Scrying Orb", 10]]
results = []
headers = ["Weapon", "Damage", "Power Attack", "Cost"]

for weapon in melee_weapons:
  name = weapon[0]
  damage = weapon[1]
  power_attack = math.pow(damage, 2)
  cost = math.pow(damage, 2.6)
  cost = int(cost)
  results.append([name, damage, power_attack, cost])

for weapon in ranged_weapons:
  name = weapon[0]
  damage = weapon[1]
  power_attack = math.pow(damage, 2.8)
  power_attack = int(power_attack)
  cost = math.pow(damage, 2.6)
  cost = int(cost)
  results.append([name, damage, power_attack, cost])

for weapon in magic_weapons:
  name = weapon[0]
  damage = weapon[1]
  power_attack = math.pow(damage, 1.6)
  power_attack = int(power_attack)
  cost = math.pow(damage, 2.6)
  cost = int(cost)
  results.append([name, damage, power_attack, cost])

output = tabulate(results, headers)
print(output)
