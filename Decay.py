# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:38:13 2020

@author: skyle
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math

lambda1 = 0.005
time_max = 2000
number = nloop = 1000000

random.seed()

t = np.arange(0, time_max + 1)
N = np.zeros(time_max + 1)
dN = np.zeros(time_max + 1)
lnN = np.zeros(time_max + 1)
lndN = np.zeros(time_max + 1)
dt = np.zeros(time_max + 1)

for time in range(0, time_max+1):
    for atom in range(1, number +1):
        decay = random.random()
        if (decay < lambda1):
            nloop = nloop - 1
        deltaN = lambda1*number/decay
        ln_N = math.log(number)
        ln_dN = math.log(deltaN)
        deltat = 1
    number = nloop
    N[time] = number
    dN[time] = deltaN
    lnN[time] = ln_N
    lndN[time] = ln_dN
    dt[time] = deltat
    print(time, number, deltaN, ln_N, ln_dN)
    
plt.xlabel("$t$")
plt.ylabel("$ln(N)$")
plt.plot(t,lnN,"-")
plt.show()

plt.xlabel("$t$")
plt.ylabel("$ln(dN)$")
plt.plot(t,lndN, "-")
plt.show()
