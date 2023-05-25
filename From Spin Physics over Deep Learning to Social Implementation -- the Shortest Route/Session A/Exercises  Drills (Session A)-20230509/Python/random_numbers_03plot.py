#!/usr/bin/env python3

"""Calculate and plot the average and variance for random numbers in the range of [0, 1).
"""

import numpy as np
import matplotlib.pyplot as plt

iseed = 42
rng = np.random.default_rng(iseed)
expo = 4
nsamples = np.power(10, range(1, expo+1))
average_diffs = np.zeros(expo)
variance_diffs = np.zeros(expo)
print('# of smpl,                sum,           average,      <r>-r_0,           variance,      σ^2 - σ_0^2')
for i, nsample in enumerate(nsamples):
    # Calculate the average and variance.
    # You can optimize (vectorize) the loop for summation by `np.sum()`.
    # rnds = rng.random(nsample)
    # summ  = np.sum(rnds)
    # summ2 = np.sum(rnds**2)
    summ  = 0
    summ2 = 0
    for _ in range(nsample):
        r = rng.random()
        summ  += r
        summ2 += r**2
    average  = summ / nsample
    variance = summ2 / nsample - average**2
    average_diffs[i]  = np.abs(average - 0.5)
    variance_diffs[i] = np.abs(variance - 1/12)
    print(f'{nsample:10} {summ:<20}',
          f'{average:<20.15} {average_diffs[i]:<14.3e}',
          f'{variance:<20.15} {variance_diffs[i]:<14.3e}')

# Plot diffrence of average and variance.
# N vs <r_i>
_fig, (ax_ave, ax_var) = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 4.5))
ax_ave.set_title('average')
ax_ave.scatter(nsamples, average_diffs)
ax_ave.set(xlim = (1, nsamples[expo-1]))
ax_ave.set_xscale('log')
ax_ave.set_yscale('log')
# N vs < (r-r_i)^2 >
ax_var.set_title('variance')
ax_var.scatter(nsamples, variance_diffs)
ax_var.set(xlim = (1, nsamples[expo-1]))
ax_var.set_xscale('log')
ax_var.set_yscale('log')
plt.show()
