# monte-carlo-matrix-multiplication
A silly matrix multiplication algorithm using the Monte Carlo method

## Why?
[Google's AlphaEvolve has recently found a new way to multiply matrices faster,](https://www.technologyreview.com/2025/05/14/1116438/google-deepminds-new-ai-uses-large-language-models-to-crack-real-world-problems) which got me thinking about interesting ways I could multiply matrices. Since I'm not smart enough to come up with a more efficient algorithm, I figured I could go in the opposite direction.

Also, it's just fun to see how ridiculous you can make a basic task.

## How to Run
Simply clone this repository and install the only dependency (numpy):
```shell
$ pip install numpy
```

Then run `monte_carlo_matrix_multiply.py`.

## Example Output
```
 --- COSINE --- 
Monte Carlo: cos(2) = -0.4141322075720344
Deterministic: cos(2) = -0.4161468365471424

--- SQUARE ROOT --- 
Monte Carlo: sqrt(4) = 1.9941500425338745
Deterministic: sqrt(4) = 2.0

--- DOT PRODUCT --- 
Vector 1: [0.1 0.4 0.9]
Vector 2: [0.4 0.1 0.5]

Monte Carlo: v1 ⋅ v2 = 0.5319975491487168
Deterministic: v1 ⋅ v2 = 0.53

--- MATRIX MUL --- 
Matrix 1:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Matrix 2:
[[3.4 9.3 4.4]
 [7.4 3.3 0.4]
 [3.9 1.1 4. ]
 [6.6 3.1 9.9]]

Monte Carlo (mat1 * mat2):
[[ 55.52450726  30.52979024  56.94256002]
 [142.0866338   99.62367296 132.01741579]
 [223.62717565 168.47200924 210.09419454]]

Deterministic (mat1 * mat2):
[[ 56.3  31.6  56.8]
 [141.5  98.8 131.6]
 [226.7 166.  206.4]]
```