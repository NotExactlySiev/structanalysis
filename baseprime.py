import cv2
import numpy as np
from sympy import sieve
from sympy.ntheory import isprime, factorint
import csv

BAR = 3
glyphs = {}

def get_glyph(number):
    if number not in glyphs.keys():
        glyphs[number] = glyph(number)

    return glyphs[number]


class glyph:
    def __init__(self, num):
        self.num = num
        self.level = 0
        self.length = 0
        self.factors = factorint(self.num)
        self.children_numbers = []
        self.children = []
        self.complexity = 0
        self.ascii = ""

        self.set_type()
        self.set_children_numbers()
        self.create_children()

        self.set_ascii()

        #self.set_complexity()

        self.set_size()
        self.set_shape()
        
        

    def set_type(self):
        if self.num == 2:
            self.type = "base"
        elif len(self.factors) > 1:
            self.type = "multi"
        else:
            if isprime(self.num):
                self.type = "prime"
            else:
                self.type = "power"

    def set_children_numbers(self):
        if self.type == "base":
            return
            
        if self.type == "prime":
            self.children_numbers.append(sieve.search(self.num)[0])
            return

        if self.type == "multi":
            for factor in self.factors.keys():
                self.children_numbers.append(factor ** self.factors[factor])
            
        if self.type == "power":
            self.children_numbers = list(list(self.factors.items())[0])

    def create_children(self):
        for number in self.children_numbers:
            self.children.append(get_glyph(number))

    def set_complexity(self):        
        if self.type == "base":
            self.complexity = 1
            return
            
        if self.type == "prime":
            self.complexity = self.children[0].complexity + 1
            return

        if self.type == "multi" or self.type == "power":
            self.complexity = 0
            for child in self.children:
                self.complexity += child.complexity

            #if self.type == "multi":
            #    self.complexity += 1

            return

    def set_ascii(self):
        if self.type == "base":
            self.ascii = "-"
        
        if self.type == "prime":
            self.ascii = "<" + self.children[0].ascii
           
        if self.type == "multi":
            self.ascii = "".join("/" + child.ascii for child in self.children[:-1])
            self.ascii += self.children[-1].ascii
            
        if self.type == "power":
            self.ascii = "\\" + self.children[0].ascii + self.children[1].ascii


    def set_size(self):
        if self.type == "base":
            self.level = 1
            self.length = BAR
            return

        if self.type == "prime":
            self.level = self.children[0].level + 1
            self.length = self.children[0].length
            return

        if self.type == "multi":
            self.level = max([child.level for child in self.children])
            self.length = sum([child.length + 1 for child in self.children]) - 1
            return

        if self.type == "power":
            self.level = self.children[0].level + self.children[1].level + 1
            self.length = self.children[0].length + self.children[1].length - 1
            return

    def set_shape(self):
        if self.num % 100000 == 0:
            print("Drawing shape for {}: ({}, {})".format(self.num, self.level, self.length))
        self.shape = np.zeros((2*self.level - 1, self.length), np.uint8)

        if self.type == "base":
            self.shape[:,:] = 255
            return
        
        if self.type == "prime":
            self.shape[0, :] = 255
            self.shape[2:, :] = self.children[0].shape
            return

        if self.type == "multi":
            xpos = 0
            for child in self.children:
                self.shape[self.level - child.level: self.level + child.level - 1,
                           xpos: xpos + child.length] = child.shape
                xpos += child.length + 1
            return

        if self.type == "power":
            base = self.children[0]
            power = self.children[1]
            #base
            self.shape[2*power.level + 1: -1, :base.length] = base.shape

            #power
            self.shape[:2*power.level - 1, base.length - 1:] = power.shape

            #power bar
            self.shape[2*power.level:,  base.length] = 255
            
            return

    def show(self):
        cv2.imshow("", cv2.resize(self.shape, None, fx=15, fy=15, interpolation=cv2.INTER_NEAREST))

get_glyph(87).show()

#data = []
#for i in range(2, 200000):
#    data.append([i, len(get_glyph(i).ascii)])

#print(data)

#f = open('data.csv', 'w')
#write = csv.writer(f)
#write.writerows(data)

"""
H = 500
W = 500

maxHeight = 2*max([get_glyph(i).level for i in range(2, H*W + 1)])
maxWidth = max([get_glyph(i).length for i in range(2, H*W + 1)])

board = np.zeros((maxHeight * H, maxWidth * W), np.uint8)

for i in range(2, H*W + 1):
    col = (i-1)%W
    row = (i-1)//H
    board[col*maxHeight:col*maxHeight + 2*get_glyph(i).level - 1, row*maxWidth:row*maxWidth + get_glyph(i).length] = get_glyph(i).shape

#board = cv2.resize(board, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
cv2.imwrite("D:\\fuck.jpg", board, [cv2.IMWRITE_JPEG_QUALITY, 85])
"""

"""
x = []
y1 = []
y2 = []

for i in range(2, 1000000 + 1):
    x.append(i)
    gph = get_glyph(i)
    y1.append(gph.length + gph.level)

fig = px.scatter(x=x, y=y1)
#fig.add_scatter(x=x, y=yheight)
fig.write_html("C:\\Users\\Sadra\\Desktop\\baseprime.html")
"""
"""
x = []
y = []

for i in range(2, 10000):
    x.append(i)
    y.append(get_glyph(i).complexity)

fig = px.scatter(x=x, y=y)
fig.write_html("C:\\Users\\Sadra\\Desktop\\compl.html")
"""

