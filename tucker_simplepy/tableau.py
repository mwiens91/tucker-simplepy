"""Contains Tucker tableau class."""

from __future__ import annotations
import numpy as np


class Tableau:
    """A Tucker tableau.

    TODO: finish docstring
    """

    def __init__(self, matrix: np.matrix):
        """TODO: docstring."""
        self.matrix = matrix
        self.m, self.n = matrix.shape

    def pivot(self, i: int, j: int) -> Tableau:
        """TODO: docstring."""
        # Initialize the pivoted matrix
        n = numpy.zeros((self.m, self.n))

        # Pivoting stuff here

    def __str__(self):
        """Display the tableau nicely."""
        # Stuff here
