"""Contains Tucker tableau class."""

from __future__ import annotations
import itertools
from typing import List, Tuple
import numpy as np


class Tableau:
    """A Tucker tableau.

    TODO: finish docstring
    """

    def __init__(self, matrix: np.matrix):
        """TODO: docstring."""
        self.matrix = matrix
        self.m, self.n = matrix.shape

    def get_all_coordinates(self) -> List[Tuple[int]]:
        """Return cartesian product of tableau dimensions."""
        return list(
            itertools.product(list(range(self.m)), list(range(self.n)))
        )

    def pivot(self, i: int, j: int) -> Tableau:
        """Pivot the tableau on point i, j.

        TODO finish docstring
        """
        # Initialize the pivoted matrix
        n = np.zeros((self.m, self.n))

        # Pivot. TODO: protect against zero division
        for x, y in self.get_all_coordinates():
            if (x, y) == (i, j):
                # Pivot entry
                n[x, y] = 1 / self.matrix[x, y]
            elif x == i:
                # Pivot row
                n[x, y] = self.matrix[x, y] / self.matrix[i, j]
            elif y == j:
                # Pivot column
                n[x, y] = -self.matrix[x, y] / self.matrix[i, j]
            else:
                n[x, y] = (
                    self.matrix[x, y] * self.matrix[i, j]
                    - self.matrix[x, j] * self.matrix[i, y]
                ) / self.matrix[i, j]

        return Tableau(n)

    def __str__(self):
        """Display the tableau nicely."""
        # TODO print it more nicely
        return str(self.matrix)
