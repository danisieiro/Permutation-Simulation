# -*- coding: utf-8 -*-

import random
import numpy as np


def shuffle_and_check(n):
    original = list(range(1, n+1))
    mixed = random.sample(original, len(original))
    correct = sum(np.array(original) == np.array(mixed))
    return correct

def permutation_simulation(n_simulations, sample):
    result = []
    for _ in range(1, n_simulations+1):
        result.append(shuffle_and_check(sample))
    
    return np.array(result)