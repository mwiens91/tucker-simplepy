[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python version](https://img.shields.io/badge/python-3.6%20|%203.7-blue.svg)](https://github.com/mwiens91/tucker-simplepy)

# tucker-simplepy

Contains helper functions for common operations when applying the
Simplex algorithm to a Tucker tableau (as outlined in "Linear
Programming and Its Applications" by James K. Strayer (1989)).

Tucker tableaus are represented by NumPy matrices (and use 0-indexing by
default unless you specify otherwise). All of these functions treat
matrices as immutable; i.e., they will not modify the matrices passed in
and will return new matrices.

The typing annotations in this module require Python >= 3.5, but you can
remove them if you want and have this run on any non-prehistoric Python
version.
