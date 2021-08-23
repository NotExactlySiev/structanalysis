from sympy.ntheory import isprime, factorint
import structsorter as ss
import plotly.express as px
import pandas as pd
import numpy as np


def numToStruct(num):
    return sorted(list(factorint(num).values()))

def structToBinary(struct):
    result = ""
    for num in struct:
        result += "1"
        result += "0"*(int(num) - 1)
    return result

def binaryToDecimal(binary):
    return int(binary, base=2)

HIGH = 50000

structs = pd.Series([numToStruct(i) for i in range(2, HIGH)])
binaries = structs.apply(structToBinary)
decimals = binaries.apply(binaryToDecimal)

raw = pd.DataFrame({"num": range(2, HIGH),
                    "struct": structs,
                    "binary": binaries,
                    "decimal": decimals})

raw.to_csv("D:\\category.csv")

#ranges = pd.DataFrame()

#for i in range(100):
#    this = pd.Series(raw[(raw["num"] >= i*100) & (raw["num"] < (i+1)*100)]['struct'].value_counts())
