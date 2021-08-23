from functools import reduce
import numpy as np
import math

def get_divisors(n):    
    return sorted(list(set(list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))))

def lcm(a, b):
    return a*b/math.gcd(a,b)

def star(a, b):
    if a >= b:
        return math.gcd(a, b)
    else:
        return lcm(a, b)

def increase_contrast(tiles):    
    highest = np.amax(tiles)
    lowest = np.amin(tiles)

    if highest == lowest:
        return tiles
    else:
        skew = 255/(highest - lowest)
        return np.uint8((tiles-lowest)*skew)

def color_matrix(mat, count):
    result = np.zeros((count, count), np.uint8)
    shades = [255/(count-1) * i for i in range(count)]
    for x in range(count):
        for y in range(count):
            result[x, y] = shades[mat[x, y]]
    return result

