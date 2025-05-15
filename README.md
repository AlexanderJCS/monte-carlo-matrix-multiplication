# monte-carlo-matrix-multiplication
A matrix multiplication algorithm in the dumbest way: using the Monte Carlo method

## How to Run
Simply clone this repository and install the only dependency (numpy):
```shell
$ pip install numpy
```

## Example Output
```
 --- COSINE --- 
 --- COSINE --- 
Monte Carlo: cos(2) = -0.4076676776596233
Deterministic: cos(2) = -0.4161468365471424

--- SQUARE ROOT --- 
Monte Carlo: sqrt(4) = 1.9912759065628052
Deterministic: sqrt(4) = 2.0

--- DOT PRODUCT --- 
Monte Carlo: [0.1 0.4 0.9] ⋅ [0.4 0.1 0.5] = 0.5326450897969198
Deterministic: [0.1 0.4 0.9] ⋅ [0.4 0.1 0.5] = 0.53

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
[[ 55.6881741   31.41770672  56.70784213]
 [140.95135885  99.11780238 130.07159266]
 [227.15182638 169.28021513 206.16904167]]

Deterministic (mat1 * mat2):
[[ 56.3  31.6  56.8]
 [141.5  98.8 131.6]
 [226.7 166.  206.4]]
```