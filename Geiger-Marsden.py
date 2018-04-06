from random import uniform

from numpy import pi, sqrt

area = 0.01 * 0.01  # m^2, the area which the alpha particles can hit
thickness = 1e-3  # m
alpha_count = 1000000

# Constants
e = 1.602e-19  # C, elementary charge
k = 8.9875517873681764e9  # Nm^2/C^2, Coulomb's constant
r = 7.3e-15  # m, radius of gold nucleus

atom_count = 5.901e28 * area * thickness  # 5.901e28 is the number of atoms in 1m^3 of gold


def shoot():
    u = uniform(0, area)
    if u <= atom_count * pi * r ** 2:  # assuming no overlap in atoms
        return True  # hit
    return False  # miss


c = 0
for i in range(0, alpha_count):
    if shoot():
        c += 1

p = c / alpha_count  # probability of hit
print(c, sqrt((area * p) / (pi * atom_count)))
