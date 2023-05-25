#!/usr/bin/env python3

"""Simulate 2-dimensional Ising model by Metropolis method.
Size: L^2
Boundary: Periodic
Initial condition: order or disorder
Index: 0-start
s = self.lattice[3][2] is placed on
  0 1 2 3 4
0 . . . . .
1 . . . . .
2 . . . . .
3 . . s . .
4 . . . . .
"""

import numpy as np
import matplotlib.pyplot as plt

class Ising2d():
    def __init__(self, L = 10, beta = 1.0, ordered = False, rng = None):
        """Initialize 2-dimensional Ising model with random numbers.
        All spins on the lattice are oriented upwards if `ordered` is True.
        """
        if rng is None:
            self.rng = np.random.default_rng(42)
        else:
            self.rng = rng
        self.L = L
        # inverse temperature β = 1/(kb*T) = 1/T (kb = 1).
        self.beta = beta
        self.init_lattice(ordered)
        self.checker_board = np.array([(i+j) % 2 for i in range(self.L) for j in range(self.L)]).reshape(self.L, self.L)
    def __str__(self):
        """Return the spins on the lattice as a string with `1` or `-1`
        """
        str = f'{self.L}x{self.L}, kbt = {self.kbt}, β = {self.beta}:'
        for i in range(self.L):
            str = str + '\n'
            for j in range(self.L):
                s = self.lattice[i][j]
                str = str + f'{s:3}'
        return str
    def init_lattice(self, ordered = False):
        """ Initialize the state of spins on the lattice by numpy array.
        Set all spin `1` if ordered is `True`.
        Set each spin `1` or `-1` randomomly if ordered is `False`.
        """
        # Allocate the lattice as the 2-dimensional numpy array (fast!).
        if (ordered):
            self.lattice = np.ones(self.L*self.L, dtype = np.int32).reshape(self.L, self.L)
        else:
            self.lattice = np.where(self.rng.random(self.L*self.L) < 0.5, 1, -1).reshape(self.L, self.L)
    @property
    def kbt(self):
        return self._kbt
    @kbt.setter
    def kbt(self, kbt):
        if (kbt <= 0):
            raise ValueError(f'kbt must be > 0; {kbt}')
        self._kbt = kbt
        self._beta  = 1/kbt
    @property
    def beta(self):
        return self._beta
    @beta.setter
    def beta(self, beta):
        if (beta <= 0):
            raise ValueError(f'beta must be > 0; {beta}')
        self._beta = beta
        self._kbt  = 1/beta
    def calc_magne(self):
        """Calculate the magnetism per spin `m`: [-1, 1].
        m = M / (L^2) = ∑_i si / (L^2).
        This method has a time complexity O(N) = O(L^2).
        """
        self.magne = np.sum(self.lattice)
        return self.magne / (self.L*self.L)
    def calc_energy(self):
        """Calculate the magnetism per spin `e` ≥ -2.
        e = E / (L^2) = -J∑_<i,j> si*sj / (L^2), (J = 1).
        This method has a time complexity O(N) = O(L^2).
        Note that this lattice has periodic boundary conditions.
        """
        spins_right = np.roll(self.lattice, -1, axis = 1)
        spins_up    = np.roll(self.lattice,  1, axis = 0)
        energy = -np.sum(self.lattice * (spins_right + spins_up))
        # energy2 = 0
        # for i in range(self.L):
        #     for j in range(self.L):
        #         # Spins on right or upperwards lattice may be boundary.
        #         s_right = self.lattice[i][(j+1) % self.L]
        #         s_up    = self.lattice[(i+1) % self.L][j]
        #         energy2 -= self.lattice[i][j] * (s_right + s_up)
        # assert(energy == energy2)
        self.energy = energy
        return self.energy / (self.L*self.L)
    def update(self):
        """Update the state of spins by Metropolis method as checkerboard.
        First update the `.` spin on the lattice ( (i+j) % 2 == 0).
        Second update the `#` spin on the lattice ( (i+j) % 2 == 1).
         012345
        0.#.#.#
        1#.#.#.
        2.#.#.#
        3#.#.#.
        4.#.#.#
        5#.#.#.
        """
        # Optimize updating by numpy.
        # This optimization is not necessary for fast programming languages.
        # `for` statement in Python3 is slow...
        rnds = self.rng.random(self.L * self.L).reshape(self.L, self.L)
        for k in range(2): # k: 0 or 1
            spins_around = np.roll(self.lattice, 1, axis = 0) + np.roll(self.lattice, -1, axis = 0) \
                + np.roll(self.lattice, 1, axis = 1) + np.roll(self.lattice, -1, axis = 1)
            # s[i, j] -> -s[i, j]
            # ΔE = -(-s[i, j] - s[i, j]) * spins_around[i, j]
            #    = 2 * s[i, j] * spins_around[i, j]
            delta_Es = 2 * self.lattice * spins_around
            cond = np.logical_and(self.checker_board == k, rnds < np.exp(-self.beta*delta_Es))
            self.lattice = np.where(cond, -self.lattice, self.lattice)

if __name__ == '__main__':
    iseed = 42
    rng = np.random.default_rng(iseed)
    # Ising2d ferromagnetic.
    kbt = 3.0 # ferromagnetic if kbt < 2.2692..., paramagnetic if kbt > 2.2692...
    is2d = Ising2d(L = 100, ordered = True, rng = rng)
    is2d.kbt = kbt
    # These condition are true because `is2d` is ordered.
    print(is2d)
    print(f'm = {is2d.calc_magne()}, e = {is2d.calc_energy()}')
    assert(is2d.calc_magne() == 1)
    assert(is2d.calc_energy() == -2)
    # Ising2d paramagnetic.
    is2d.init_lattice(ordered = False)
    print(is2d)
    print(f'm = {is2d.calc_magne()}, e = {is2d.calc_energy()}')
    # Set maixmum Monte Carlo step.
    max_mcs_discard = 10000
    for mcs in range(max_mcs_discard):
        print(f'Updating ... {mcs+1}:')
        is2d.update()
    max_mcs = 50000
    sum_m = 0
    sum_e = 0
    for mcs in range(max_mcs):
        print(f'Updating ... {mcs+1}: ', end = '')
        is2d.update()
        m = is2d.calc_magne()
        sum_m += m
        e = is2d.calc_energy()
        sum_e += e
        print(f'm = {m:<5.2}, e = {e:<5.3}')
    average_m = sum_m / max_mcs
    average_e = sum_e / max_mcs
    print(f'{is2d.kbt} {average_m:<5.2} {average_e:<5.3}')
    # Plot lattice.
    fig, ax = plt.subplots(figsize = (5, 5))
    ax.pcolor(is2d.lattice, cmap = plt.cm.winter) # heatmap
    plt.show()
