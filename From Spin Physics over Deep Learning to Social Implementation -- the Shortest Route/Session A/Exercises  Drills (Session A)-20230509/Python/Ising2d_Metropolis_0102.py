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
        energy = 0
        for i in range(self.L):
            for j in range(self.L):
                # Spins on right or upperwards lattice may be boundary.
                s_right = self.lattice[i][(j+1) % self.L]
                s_up    = self.lattice[(i+1) % self.L][j]
                energy -= self.lattice[i][j] * (s_right + s_up)
        self.energy = energy
        return self.energy / (self.L*self.L)
    def update(self):
        """Update the state of spins by Metropolis method as checkerboard.
        First update the `.` spin on the lattice.
        Second update the `#` spin on the lattice.
        row: i, column: j
         012345
        0.#.#.#
        1#.#.#.
        2.#.#.#
        3#.#.#.
        4.#.#.#
        5#.#.#.
        """
        update_count = np.zeros(self.L * self.L).reshape(self.L, self.L)
        for k in range(2): # k: 0 or 1
            for i in range(self.L):
                start = (k + (i&1)) % 2 # k if i = 0, 2, ..., self.L-2 , (k+1) % 2 if i = 1, 3, ..., self.L-1 .
                for j in range(start, self.L, 2):
                    self.update_spin(i, j)
                    update_count[i][j] += 1
        assert(np.all(update_count == 1))
    def update_spin(self, y, x):
        """Update a state of spin on the site (x, y).
        """
        # Spin on the site (x, y).
        s_bef = + self.lattice[y][x]
        s_aft = - self.lattice[y][x]
        # Spins around the site (y, x).
        s_right = self.lattice[y][(x+1) % self.L]
        s_up    = self.lattice[(y+1) % self.L][x]
        s_left  = self.lattice[y][(x-1+self.L) % self.L]
        s_down  = self.lattice[(y-1+self.L) % self.L][x]
        # ΔE = E_aft - E_bef
        energy_bef = - s_bef * (s_right + s_up + s_left + s_down)
        energy_aft = - s_aft * (s_right + s_up + s_left + s_down)
        delta_energy = energy_aft - energy_bef
        # Metropolis flip.
        # Flip spin with a probability of `min(exp(-βΔE), 1)`.
        if self.rng.random() < np.exp(-self.beta * delta_energy):
            self.lattice[y][x] = s_aft

if __name__ == '__main__':
    iseed = 42
    rng = np.random.default_rng(iseed)
    # Ising2d ferromagnetic.
    kbt = 2.2692 # ferromagnetic if kbt < 2.2692..., paramagnetic if kbt > 2.2692...
    is2d = Ising2d(L = 20, ordered = True, rng = rng)
    is2d.kbt = kbt
    # These condition are true because `is2d` is ferromagnetic.
    assert(is2d.calc_magne() == 1)
    assert(is2d.calc_energy() == -2)
    print(is2d)
    # Ising2d paramagnetic.
    is2d.init_lattice(ordered = False)
    print(is2d)
    print(f'm = {is2d.calc_magne():<5.2}, e = {is2d.calc_energy():<5.3}')
    is2d.update()
    print(is2d)
    print(f'm = {is2d.calc_magne():<5.2}, e = {is2d.calc_energy():<5.3}')
    # Plot lattice.
    fig, ax = plt.subplots(figsize = (5, 5))
    ax.pcolor(is2d.lattice, cmap = plt.cm.winter) # heatmap
    plt.show()
