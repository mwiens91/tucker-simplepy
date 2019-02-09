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
        self.n, self.m = matrix.shape

    def get_all_coordinates(self) -> List[Tuple[int]]:
        """Return cartesian product of tableau dimensions."""
        return list(
            itertools.product(list(range(self.n)), list(range(self.m)))
        )

    def pivot(self, i: int, j: int) -> Tableau:
        """Pivot the tableau on entry with row i, column j.

        TODO finish docstring
        """
        # Initialize the pivoted matrix
        n = np.zeros((self.n, self.m))

        # Pivot. TODO: protect against zero division
        for row, col in self.get_all_coordinates():
            if (row, col) == (i, j):
                # Pivot entry
                n[row, col] = 1 / self.matrix[row, col]
            elif row == i:
                # Pivot row
                n[row, col] = self.matrix[row, col] / self.matrix[i, j]
            elif col == j:
                # Pivot column
                n[row, col] = -self.matrix[row, col] / self.matrix[i, j]
            else:
                n[row, col] = (
                    self.matrix[row, col] * self.matrix[i, j]
                    - self.matrix[row, j] * self.matrix[i, col]
                ) / self.matrix[i, j]

        return Tableau(n)

    def __str__(self):
        """Display the tableau nicely."""
        # TODO print it more nicely
        return str(self.matrix)
