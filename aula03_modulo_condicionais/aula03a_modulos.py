import math

from astroid.brain.brain_numpy_random_mtrand import numpy_random_mtrand_transform

num = 4
raiz = math.sqrt(4)
print(f"raiz de {num} é {round(raiz,2)}")

graus = 90
radiano = graus / 180 * math.pi
print(f"{graus} graus são {radiano:.2f} radianos ")

seno = math.sin(radiano)
print(seno)

import random

numpy_random_mtrand_transform()

num_random = random.random()
print(num_random)

num_rand_int = random.randint(1, 10)
print(num_rand_int)