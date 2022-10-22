import os
from multiprocessing import Process, Array
import math


class pythoTrip:
    def __init__(self):
        self.n = 0
        self.i = 0

    def pythagorean_triplet(self, n, p ):
        for b in range(n):
            for a in range(1, b):
                c = math.sqrt(a * a + b * b)
                if c % 1 == 0:
                    print(a, b, int(c))


if __name__ == "__main__":
    for pythagoreanTriplets in range(1, os.cpu_count()):
        n = int(5000/pythagoreanTriplets)
        triplets = []
        processes = []
        shared_i = Array('i', [0]*pythagoreanTriplets)
        shared_n = Array('i', [0]*pythagoreanTriplets)
        for i in range(pythagoreanTriplets):
            triplets.append(pythoTrip())
            processes.append(Process(target=triplets[i].pythagorean_triplet, args=(n, i, shared_i, shared_n)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()


