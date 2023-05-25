#!/usr/bin/env python3

"""Display the random numbers.
"""

import numpy as np

# Results depend on the initial seed.
iseed = 42
rng = np.random.default_rng(iseed)
n = 10
for i in range(n):
    r = rng.random()
    print(f'{i:10} {r:<30.15}')
