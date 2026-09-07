# -*- coding: utf-8 -*-
### SOC612: Data Analytics for the Social Sciences
### Date: September 8, 2026
### Author: Raphi Duerr
### Lecture 1: Introduction

# Hello World!

# This is a Python (.py) script. Let's test a few commands to see if everything runs
# correctly:

print(2 + 8)
print(2 == 8)
print(2 > 8 or 2 < 8)
print(2 > 8 and 2 < 8)
import math
print(math.sqrt(81))

# If everything is ok so far, let's do a few more:

import numpy as np

v = np.arange(1, 11)
x = np.arange(91, 101)
w = np.array(["HK", "NT", "KLN"])

print(v.dtype)  
print(w.dtype)  
print(len(v))   
print(np.unique(w))

a = x + v
b = x * v
c = x - v
d = v / 3

data = np.column_stack((a, b, c, d))
print(data)

# Final test: import pandas (tidyverse equivalent)
# To install required packages: pip install numpy pandas
import pandas as pd
print("pandas imported successfully (tidyverse equivalent)")