# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:40:13 2024

@author: pc
"""

from src import functions
import matplotlib.pyplot as plt
import numpy as np

simulations = 1000
n_things = 10

result = functions.permutation_simulation(simulations, n_things)
plt.hist(result, bins=[0,1,2,3,4,5,6,7,8,9,10], weights=np.zeros_like(result) + 1. / result.size)
plt.xlabel('Correct choice')
plt.ylabel('Macthes')
