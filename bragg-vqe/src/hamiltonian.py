import numpy as np


def bragg_hamiltonian(delta: float, omega: float) -> np.ndarray:
    """3-state truncated Bragg Hamiltonian in the {|-1>, |0>, |+1>} momentum basis."""
    return np.array(
        [
            [4 + delta, omega, 0],
            [omega, 0, omega],
            [0, omega, 4 - delta],
        ],
        dtype=float,
    )
