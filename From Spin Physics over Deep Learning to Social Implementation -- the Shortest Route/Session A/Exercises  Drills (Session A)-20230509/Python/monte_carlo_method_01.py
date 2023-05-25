#!/usr/bin/env python3

"""Estimate the approximate value of π by the module `MCMethod.py`.
See `MonteCarloMethod.run` in `MCMethod.py` if you want to know this algorithm.
"""

import numpy as np
class MonteCarloMethod():
    """Estimate the approximate value of π by
    calculating the area of the circle with radius 1 (= π) by Monte Carlo integration.
    """
    def __init__(self, rng = None):
        """Initialize `rng` (random number generator).
        Its method can generate random numbers (0 <= rnd.random() < 1).
        """
        if rng is None:
            self.rng = np.random.default_rng(42)
        else:
            self.rng = rng

    def run(self, times):
        """Generate random numbers (x, y) where 0 <= x < 1 dna 0 <= y < 1,
        and count the number of points within a circle of raidus 1.
        The area of the circle of radius 1 in x > 0 and y > 0 is S = (πr^2)/4 = π/4 (when r == 1).
                   1|-----
                    |    ----
                    | (x, y) --
                    |         -
        ------------|------------
                   0|         1
                    |
                    |
                    |
        `cnts` / `times` ≃ S.
        `cnts` / `times` ≃ π/4
        4 * `cnts` / `times` ≃ π.
        """
        cnts = 0
        for _ in range(0, times):
            x = self.rng.random()
            y = self.rng.random()
            if x**2 + y**2 <= 1:
                cnts += 1
        return 4 * cnts / times

iseed = 42
rng = np.random.default_rng(iseed)
mcm = MonteCarloMethod(rng = rng)
# Calculate π for n = 10^1 ~ 10^7.
t = 1000
pi_calc = mcm.run(t)
pi_diff = np.abs(pi_calc - np.pi)
print('# of smpl,                  pi, absoluet difference')
print(f'{t:10} {pi_calc:20.15f} {pi_diff:14e}')
