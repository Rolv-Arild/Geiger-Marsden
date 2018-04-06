from random import uniform

from numpy import pi, sqrt

area = 0.01 * 0.01  # m^2, the area which the alpha particles can hit: 1cm x 1cm
thickness = 1e-3  # m, the thickness of the gold foil: 1mm
alpha_count = 1000000  # the number of alpha particles to shoot at the foil

# Constants
r = 7.3e-15  # m, true radius of gold nucleus

atom_count = 5.901e28 * area * thickness  # 5.901e28 is the number of atoms in 1m^3 of gold


# Shoots an alpha particle and determines if it was a hit or a miss
def shoot():
    u = uniform(0, area)
    if u <= atom_count * pi * r ** 2:  # assuming no overlap in atoms
        return True  # hit
    return False  # miss


hit_count = 0
for i in range(0, alpha_count):  # shoots all the alpha particles
    if shoot():
        hit_count += 1

p = hit_count / alpha_count  # probability of hit
print(hit_count, sqrt((area * p) / (pi * atom_count)))
