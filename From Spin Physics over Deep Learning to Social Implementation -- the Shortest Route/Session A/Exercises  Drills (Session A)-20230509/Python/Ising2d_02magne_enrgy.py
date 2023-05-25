#!/usr/bin/env python3

"""Create 2-dimensional Ising model.
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
        # Allocate the lattice as the list of list of int (slow!).
        self.lattice = [[0] * self.L for _ in range(self.L)]
        self.init_lattice(ordered)
    def __str__(self):
        """Return the spins on the lattice as a string with `1` or `-1`
        """
        str = f'{self.L}x{self.L}, β = {self.beta}:'
        for i in range(self.L):
            str = str + '\n'
            for j in range(self.L):
                s = self.lattice[i][j]
                str = str + f'{s:3}'
        return str
    def init_lattice(self, ordered = False):
        """ Initialize the state of spins on the lattice.
        Set all spin `1` if ordered is `True`.
        Set each spin `1` or `-1` randomomly if ordered is `False`.
        """
        for i in range(self.L):
            for j in range(self.L):
                if ordered:
                    self.lattice[i][j] = 1
                else:
                    r = self.rng.random()
                    # print(f'({i}, {j}): {r}, {r < 0.5}')
                    self.lattice[i][j] = 1 if r < 0.5 else -1
    def calc_magne(self):
        """Calculate the magnetism per spin `m`: [-1, 1].
        m = M / (L^2) = ∑_i si / (L^2).
        This method has a time complexity O(N) = O(L^2).
        """
        magne = 0
        for i in range(self.L):
            for j in range(self.L):
                magne += self.lattice[i][j]
        self.magne = magne
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

if __name__ == '__main__':
    import numpy as np
    iseed = 42
    rng = np.random.default_rng(iseed)
    # Ising2d ferromagnetic.
    is2d = Ising2d(L = 20, ordered = True, rng = rng)
    # These condition are true because `is2d` is ordered.
    assert(is2d.calc_magne() == 1)
    assert(is2d.calc_energy() == -2)
    print('ferromagnetic')
    print(is2d)
    print(f'm = {is2d.calc_magne()}, e = {is2d.calc_energy()}')
    # Ising2d paramagnetic.
    is2d.init_lattice(ordered = False)
    print('paramagnetic')
    print(is2d)
    print(f'm = {is2d.calc_magne()}, e = {is2d.calc_energy()}')
    # Plot lattice.
    fig, ax = plt.subplots(figsize = (5, 5))
    ax.pcolor(is2d.lattice, cmap = plt.cm.Greens) # heatmap
    plt.show()
