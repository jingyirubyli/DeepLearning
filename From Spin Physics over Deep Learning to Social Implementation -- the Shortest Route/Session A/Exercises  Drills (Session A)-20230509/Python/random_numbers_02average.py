#!/usr/bin/env python3

"""Calculate the average and variance for random numbers in the range of [0, 1).
"""

import numpy as np
import matplotlib.pyplot as plt

iseed = 42
rng = np.random.default_rng(iseed)
expo = 5
nsample = 10 ** expo
# Calculate the average and variance.
# You can also calculate the average by `np.sum(np.random.random(nsample)) / nsample` using numpy.
summ  = 0
summ2 = 0
for _ in range(nsample):
    r = rng.random()
    summ  += r
    summ2 += r**2
average  = summ / nsample
variance = summ2 / nsample - average**2
average_diff  = np.abs(average - 0.5)
variance_diff = np.abs(variance - 1/12)
print('# of smpl,                sum,           average,      <r>-r_0,           variance,      σ^2 - σ_0^2')
print(f'{nsample:10} {summ:<20}',
      f'{average:<20.15} {average_diff:<14.3e}',
      f'{variance:<20.15} {variance_diff:<14.3e}')
