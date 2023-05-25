#!/usr/bin/env python3

"""Simulated annealing.
2-dimensional Ising model:
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
interactions:
J[i, j]
"""

import numpy as np
import matplotlib.pyplot as plt

class Ising2d():
    def __init__(self, beta = 1.0, ordered = False, rng = None):
        """Initialize 2-dimensional Ising model with random numbers.
        All spins on the lattice are oriented upwards if `ordered` is True.
        """
        if rng is None:
            self.rng = np.random.default_rng(42)
        else:
            self.rng = rng
        self.L = 100
        # inverse temperature β = 1/(kb*T) = 1/T (kb = 1).
        self.beta = beta
        self.init_lattice(ordered)
        self.checker_board = np.array([(i+j) % 2 for i in range(self.L) for j in range(self.L)]).reshape(self.L, self.L)
        # ferromagnetic interaction if J[i][j] == J[i][j+1], antiferromagnetic integration if J[i][j] /= J[i][j+1].
        self.init_interaction()
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
    def init_interaction(self):
        self.J = -np.ones(self.L * self.L).reshape(self.L, self.L)
        # Eyes
        for i in range(60, 70 + 1):
            for j in range(25, 30 + 1):
                self.J[i][j] = 1
            for j in range(65, 70 + 1):
                self.J[i][j] = 1
        # Mouth
        for i in  range(35, 40 + 1):
            for j in range(25, 75 + 1):
                self.J[i][j] = 1
        # Circle
        for i in range(self.L):
            L_half = (self.L-1) / 2
            y = (i-L_half)/L_half
            j = int(+L_half * np.sqrt(1 - y**2) + L_half)
            self.J[i][j] = 1
            j = int(-L_half * np.sqrt(1 - y**2) + L_half)
            self.J[i][j] = 1
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
        spins_right = np.roll(self.J * self.lattice, -1, axis = 1)
        spins_up    = np.roll(self.J * self.lattice,  1, axis = 0)
        energy = -np.sum(self.J * self.lattice * (spins_right + spins_up))
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
            J_lattice = self.J * self.lattice
            spins_around = np.roll(J_lattice, 1, axis = 0) + np.roll(J_lattice, -1, axis = 0) \
                + np.roll(J_lattice, 1, axis = 1) + np.roll(J_lattice, -1, axis = 1)
            # s[i, j] -> -s[i, j]
            # ΔE = -(-J[i, j]*s[i, j] - J[i, j]*s[i, j]) * spins_around[i, j]
            #    = 2 * J[i, j]*s[i, j] * spins_around[i, j]
            delta_Es = 2 * J_lattice * spins_around
            cond = np.logical_and(self.checker_board == k, rnds < np.exp(-self.beta*delta_Es))
            self.lattice = np.where(cond, -self.lattice, self.lattice)

if __name__ == '__main__':
    iseed = 42
    rng = np.random.default_rng(iseed)
    # Ising2d paramagnetic.
    is2d = Ising2d(ordered = False, rng = rng)
    fig, (ax_l, ax_J) = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 4.5))
    ax_l.pcolor(is2d.lattice, cmap = plt.cm.winter) # heatmap
    ax_l.set_title('spin configuration (initial)')
    ax_J.pcolor(is2d.J, cmap = plt.cm.winter) # heatmap
    ax_J.set_title('interaction')
    plt.show()
    # Monte Carlo Simulation
    start, end, step = 3.01, 0.01, -0.1
    temperatures = np.arange(start, end+step, step)
    # Set maixmum Monte Carlo step.
    max_mcs_discard = 1000
    for i, kbt in enumerate(temperatures):
        is2d.kbt = kbt
        nprint, nprint_by = 1, 1
        # print(f'Updating ... {is2d.kbt}:')
        for mcs in range(max_mcs_discard):
            # if mcs + 1 == nprint:
            #     print(f'Updating ... {is2d.kbt}, {mcs+1}:')
            #     if mcs + 1 == 10*nprint_by:
            #         nprint_by *= 10
            #     nprint += nprint_by
            is2d.update()
        # print(f'{kbt}, {np.abs(kbt - int(kbt))}')
        if np.abs(kbt - int(kbt)) < 0.1:
            fig, (ax_l, ax_J) = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 4.5))
            ax_l.pcolor(is2d.lattice, cmap = plt.cm.winter) # heatmap
            ax_l.set_title(f'spin configuration (T = {is2d.kbt})')
            ax_J.pcolor(is2d.J, cmap = plt.cm.winter) # heatmap
            ax_J.set_title(f'interaction')
            plt.show()
            # smile? -_-
