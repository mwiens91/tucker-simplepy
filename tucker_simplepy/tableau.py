"""Contains helpers for applying the simplex algorithm to a Tucker tableau.

Tucker tableaus are represented by NumPy matrices (and use 0-indexing by
default unless you specify otherwise). All of these functions treat
matrices as immutable; i.e., they will not modify the matrices passed in
and will return new matrices.

The typing annotations in this module require Python >= 3.5.
"""

import itertools
from typing import List, Tuple
import numpy as np


def _get_all_coordinates(matrix: np.matrix) -> List[Tuple[int]]:
    """Return cartesian product of matrix dimensions.

    Args:
        matrix: A NumPy matrix representing a tableau.
    """
    n, m = matrix.shape

    return list(itertools.product(list(range(n)), list(range(m))))


def remove_row(
    matrix: np.matrix, i: int, index_by_1: bool = False
) -> np.matrix:
    """Remove the ith row from a matrix.

    Args:
        matrix: A NumPy matrix representing a tableau.
        i: The row to remove.
        index_by_1: Whether to index by 1 (cf. indexing by 0).

    Returns:
        A matrix corresponding to the tableau with the ith row removed.
    """
    # Handle possible 1-indexing
    if index_by_1:
        i += 1

    return np.delete(matrix, (i), axis=0)


def remove_col(
    matrix: np.matrix, j: int, index_by_1: bool = False
) -> np.matrix:
    """Remove the jth column from a matrix.

    Args:
        matrix: A NumPy matrix representing a tableau.
        j: The column to remove.
        index_by_1: Whether to index by 1 (cf. indexing by 0).

    Returns:
        A matrix corresponding to the tableau with the jth column
        removed.
    """
    # Handle possible 1-indexing
    if index_by_1:
        j += 1

    return np.delete(matrix, (j), axis=1)


def pivot(
    matrix: np.matrix, i: int, j: int, index_by_1: bool = False
) -> np.matrix:
    """Pivot the tableau on entry with row i, column j.

    Args:
        matrix: A NumPy matrix representing a tableau.
        i: The row to pivot on.
        j: The column to pivot on.
        index_by_1: Whether to index by 1 (cf. indexing by 0).

    Returns:
        A matrix corresponding to the tableau after pivoting on (i, j).
    """
    # Handle possible 1-indexing
    if index_by_1:
        i, j = (i + 1, j + 1)

    # Initialize the pivoted matrix
    output = np.zeros(matrix.shape)

    # Pivot
    for row, col in _get_all_coordinates(matrix):
        if (row, col) == (i, j):
            # Pivot entry
            output[row, col] = 1 / matrix[row, col]
        elif row == i:
            # Pivot row
            output[row, col] = matrix[row, col] / matrix[i, j]
        elif col == j:
            # Pivot column
            output[row, col] = -matrix[row, col] / matrix[i, j]
        else:
            output[row, col] = (
                matrix[row, col] * matrix[i, j]
                - matrix[row, j] * matrix[i, col]
            ) / matrix[i, j]

    return output
