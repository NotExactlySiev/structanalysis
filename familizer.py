from sympy.ntheory import isprime, factorint
import structsorter as ss
import pandas as pd

class intStructure:
    def __init__(self, num):
        self.num = num
        self.structure = self.get_structure()

    def get_structure(self):
        return sorted(list(factorint(self.num).values()))

    def __str__(self):
        result = ""
        for i in self.structure:
            result += str(i)
        return result

END = 50000
raw_data = {}

keys = []
counts = {}


for i in range(2, END + 1):
    struct = intStructure(i)
    raw_data[i] = str(struct)

for i in range(2, END + 1):
    if raw_data[i] not in keys:
        keys.append(raw_data[i])
        counts[raw_data[i]] = 0

    counts[raw_data[i]] += 1

keys.sort()
for key in keys:
    pr = "]"*(counts[key]//100)
    #pr = counts[key]
    print("{}: {}".format(ss.string_to_int(str(key)), pr))


#---------------------------------------------
'''
x = [ss.string_to_int(key) for key in counts.keys()]
y = list(counts.values())

fig = px.bar(x=x, y=y)
#fig.add_scatter(x=x, y=yheight)
fig.write_html("C:\\Users\\Sadra\\Desktop\\famili.html")
'''
