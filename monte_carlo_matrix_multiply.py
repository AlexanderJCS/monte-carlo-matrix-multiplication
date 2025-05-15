import numpy as np


def monte_carlo_cos(x: float, samples: int = 1000) -> float:
    """
    Computes the cosine of x using the Monte Carlo method. Estimates the integral:
    \\int_{0}^{x}-\\sin t dt+1

    Uses the fact that d/dx cos x = -sin x

    :param x: cos(x)
    :param samples: The number of samples to use
    :return: The estimated cosine of x
    """

    rand = np.random.uniform(0, x, samples)

    # It's a bit ironic that I'm using sin to eval cos using the monte carlo method,
    #  but I would need cos to eval sin in a monte carlo sin algorithm
    neg_sin_x = -np.sin(rand)

    return np.sum(neg_sin_x) * x / samples + 1


def quake_isqrt(number: float | np.ndarray):
    # Adapted slightly from: https://ajcr.net/fast-inverse-square-root-python/
    three_halves = 1.5
    x2 = number * 0.5
    y = np.float32(number)

    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    y = i.view(np.float32)

    y = y * (three_halves - (x2 * y * y))
    return np.float32(y)


def monte_carlo_sqrt(x: float, samples: int = 100000) -> float:
    """
    Computes the square root of x using the Monte Carlo method. Estimates the integral:
    \\int_{0}^{x}\\frac{1}{2\\sqrt{t}}dt

    Uses the fact that d/dx sqrt(x) = 1/(2 * sqrt(x))

    :param x: sqrt(x)
    :param samples: The number of samples to use
    :return: The estimated square root of x
    """

    rand = np.random.uniform(0, x, samples)

    # Again, ironic that we have to use a sqrt to compute the sqrt
    #  To keep with the theme of estimation, I'm going to use the fast inverse sqrt algorithm from Quake
    half_inverse_sqrt = 0.5 * quake_isqrt(rand)

    return np.sum(half_inverse_sqrt) * x / samples


def monte_carlo_magnitude(v: np.ndarray) -> float:
    return monte_carlo_sqrt((v ** 2).sum())


def monte_carlo_dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    if v1.ndim != v2.ndim:
        raise ValueError(f"Cannot compute dot product between vectors of different sizes: {v1.ndim=}, {v2.ndim=}")

    mag_v1 = monte_carlo_magnitude(v1)
    mag_v2 = monte_carlo_magnitude(v2)

    mag_v1_minus_v2 = monte_carlo_magnitude(v1 - v2)

    # Use law of cosines
    cos_v1_v2 = (mag_v1 ** 2 + mag_v2 ** 2 - mag_v1_minus_v2 ** 2) / (2 * mag_v1 * mag_v2)

    # Use geometric dot product definition: ||v1|| * ||v2|| * cos(theta)
    return mag_v1 * mag_v2 * cos_v1_v2


def monte_carlo_matrix_mul(m1: np.ndarray, m2: np.ndarray) -> np.ndarray:
    if m1.shape[0] != m2.shape[1]:
        raise ValueError("Incompatible shapes for matrix multiplication")

    m_out = np.zeros((m1.shape[0], m2.shape[1]))

    for row_i, row in enumerate(m1):
        for col_i, col in enumerate(m2.T):
            dot_product = monte_carlo_dot_product(row, col)
            m_out[row_i, col_i] = dot_product

    return m_out


def main():
    cos_value = 2
    print(" --- COSINE --- ")
    print(f"Monte Carlo: cos({cos_value}) = {monte_carlo_cos(2)}")
    print(f"Deterministic: cos({cos_value}) = {np.cos(cos_value)}")

    sqrt_value = 4
    print("\n--- SQUARE ROOT --- ")
    print(f"Monte Carlo: sqrt({sqrt_value}) = {monte_carlo_sqrt(2)}")
    print(f"Deterministic: sqrt({sqrt_value}) = {np.sqrt(sqrt_value)}")

    v1 = np.array([0.1, 0.4, 0.9])
    v2 = np.array([0.4, 0.1, 0.5])
    print("\n--- DOT PRODUCT --- ")
    print(f"Monte Carlo: {v1} ⋅ {v2} = {monte_carlo_dot_product(v1, v2)}")
    print(f"Deterministic: {v1} ⋅ {v2} = {np.dot(v1, v2)}")

    print("\n--- MATRIX MUL --- ")
    mat1 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]])

    mat2 = np.array([
        [3.4, 9.3, 4.4],
        [7.4, 3.3, 0.4],
        [3.9, 1.1, 4.0],
        [6.6, 3.1, 9.9]
    ])

    print(f"Matrix 1:\n{mat1}\n")
    print(f"Matrix 2:\n{mat2}\n")

    print(f"Monte Carlo (mat1 * mat2):\n{monte_carlo_matrix_mul(mat1, mat2)}\n")
    print(f"Deterministic (mat1 * mat2):\n{mat1 @ mat2}\n")

if __name__ == "__main__":
    main()
