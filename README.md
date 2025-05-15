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
Monte Carlo: cos(2) = -0.40589063932644187
Deterministic: cos(2) = -0.4161468365471424

--- SQUARE ROOT --- 
Monte Carlo: sqrt(4) = 1.4178425073623657
Deterministic: sqrt(4) = 2.0

--- DOT PRODUCT --- 
Monte Carlo: [0.1 0.4 0.9] ⋅ [0.4 0.1 0.5] = 0.5264415194678744
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
[[ 55.33253043  31.44782866  56.62825449]
 [139.35862465  97.49861254 130.33164953]
 [224.75315863 165.89530182 210.86560426]]

Deterministic (mat1 * mat2):
[[ 56.3  31.6  56.8]
 [141.5  98.8 131.6]
 [226.7 166.  206.4]]
```