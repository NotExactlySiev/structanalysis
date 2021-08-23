def binary(num):
    result = []
    while (num >= 1):
        rem = num%2
        result.append(rem)
        num //= 2
    return result[::-1]

def decimal(bina):
    result = 0
    power = len(bina)
    while (power > 0):
        power -= 1
        result += bina[-power-1] * 2**(power)
    return result

def trans(num):
    result = []
    temp = binary(num)
    for digit in temp:
        if digit == 1:
            result.append(1)
        else:
            result[-1] += 1
    return result

def int_to_string(num):
    result = ""
    lis = trans(num)
    for i in lis:
        result += str(i)
    return result

def string_to_int(st):
    binary = []
    for char in st:
        binary.append(1)
        binary.extend((int(char) - 1)*[0])

    return decimal(binary)
    

    
