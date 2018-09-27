# networktools
- Python function package for network analysis.

# chord_diagram.py
- Usage: chord_diagram.py matrix.csv
- Upper triangle part of the input.csv (neighbor matrix) converted to the chord diagram.

# matrix_Z2R.py
- Usage: python3 matrix_Z2R.py [input] [output]
- Converting matrix converted by Fisher's Z conversion to the correlation matrix.

# Rmat_significant.py
- Usage: python3 Rmat_significant.py [input] [output] [number of samples] [significance level]
- Get R matrix with only significant and positive values.

# tnorm_r2len.py
- Usage: python3 [input] [output]
- Converting correlation matrix to length matrix by Dombi t-norm.

# tnorm_len2wei.py
- Usage: python3 [input] [output]
- Converting length matrix to weight matrix by Dombi t-norm.
