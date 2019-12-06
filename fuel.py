from math import floor

def fuel(mass: float):
    return floor(mass / 3) - 2

def recursive_fuel(mass: float):
    restante = fuel(float(mass))
    if (restante > 0):
        fuel_recalculated.append(restante)
        recursive_fuel(restante)

fuel_calculate = []
fuel_recalculated = []

with open('fuels.txt', 'r') as file:
    line = file.readline()
    while line:
        fuel_calculate.append(fuel(float(line)))
        recursive_fuel(float(line))
        line = file.readline()

print(sum(fuel_calculate))
print(sum(fuel_recalculated))