#!/usr/bin/env python3

"""Calculate the correlation for random numbers in the range of [0, 1).
"""

import numpy as np
import matplotlib.pyplot as plt

iseed = 42
rng = np.random.default_rng(iseed)
nsample = 10 ** 4
rnds = rng.random(nsample + 5)
print(f'        x, # of smpl,     correlation, absolute difference')
for x in range(1, 5 + 1): # x: [1, 5]
    # Calculate the correlation.
    # np.sum(vec1 * vec2) == inner_product(vec1, vec2) == rnds[0, 1, ..., n] · rnds[x, x, ..., n+x-1]
    correlation = np.sum(rnds[0:nsample-1] * rnds[x:nsample+x-1]) / nsample
    corr_diff   = np.abs(correlation - 1/4)
    print(f'{x:10} {nsample:10} {correlation:<20.15} {corr_diff:<14.3e}')
