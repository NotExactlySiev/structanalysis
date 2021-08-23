from sutils import get_snum

for i in range(2, 10000):
    print(get_snum(i).get_divisors_list())
