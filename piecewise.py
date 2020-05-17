#!/usr/bin/env python3

import math
import numpy as np
import pandas as pd

# define the function for v
def fun (t): 
    # test case
    if 0 <= t <= 10:
        return float((11*t)**2) - float(5*t)
    elif 10  <= t <= 20:
        return float(1100-5*t)
    elif 20 <= t <=30:
        return 50*t + 2*((t-20)**2)
    elif t > 30:
        return float(1520*math.exp(-0.2*(t-30)))
    # otherwise
    return 0.0 

vfun = np.vectorize(fun)
# get intervals which is 0.5. Meaning its the total number multiplied by two
intervals=((-5-50)*-1)*2

# set the start stop and the intervals(total number of items)
t = np.linspace(-5, 50,num=intervals)
# set v which is a function of t  
v = vfun(t)

# set the number of rows to be displayed to the total number of items
pd.set_option('display.max_rows', intervals)
# create the table with pandas
df = pd.DataFrame({"t": t, "v": v})
# round the items to three decimal places to show -5
df=df.round(1)
# print your table
print(df)