import os
from multiprocessing import Process, Array
import math


class pythoTrip:
    def __init__(self):
        self.n = 0
        self.i = 0

    def pythagorean_triplet(self, n):
        for b in range(n):
            for a in range(1, b):
                c = math.sqrt(a * a + b * b)
                if c % 1 == 0:
                    print(a, b, int(c))

pythotrip = pytho_trip()
pythotrip.pythagorean_triplet(100)



