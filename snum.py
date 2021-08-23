import smath
import numpy as np
import math

class snum:
    def __init__(self, num):
        self.num = num

        self.divisors = []
        self.count = 0
        self.indexes = None
        self.has_indexes = False

    def get_divisors_list(self):
        if not self.divisors:
            self.divisors = smath.get_divisors(self.num)

        return self.divisors

    def get_divisor(self, index):
        if index < 0 or index >= self.count:
            return 0
        
        return self.get_divisors_list()[index]

    def get_divisor_index(self, num):
        if num not in self.get_divisors_list():
            return -1

        return self.get_divisors_list().index(num)


    def get_count(self):
        if self.count == 0:
            self.count = len(self.get_divisors_list())

        return self.count
    
    def get_indexes(self, normalized=True):
        if not self.has_indexes:
            size = self.get_count()
            center = size//2
            self.indexes = np.zeros((size, size), np.int32)
            for x in range(self.get_count()):
                for y in range(self.get_count()):
                    divisor = math.gcd(self.get_divisor(x), self.get_divisor(y))
                    index = self.get_divisor_index(divisor)
                    
                    if normalized:
                        index += (center - min(x, y))

                    self.indexes[x, y] = index

            self.has_indexes = True

        return self.indexes

    def get_std(self):
        return np.std(self.get_indexes())

    def get_entropy(self):
        return sum([len(np.unique(row))-1 for row in self.get_indexes()])\
                /(self.get_count())  
