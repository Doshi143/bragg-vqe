from itertools import product

import numpy as np
from qiskit.quantum_info import Pauli, SparsePauliOp


def padded_bragg_hamiltonian(delta: float, omega: float, penalty: float = 13.0) -> np.ndarray:
    """4x4 two-qubit encoding of the Bragg Hamiltonian with a penalty on the unused |11> state."""
    return np.array(
        [
            [4 + delta, omega, 0, 0],
            [omega, 0, omega, 0],
            [0, omega, 4 - delta, 0],
            [0, 0, 0, penalty],
        ],
        dtype=float,
    )


def pauli_decompose(matrix: np.ndarray, tolerance: float = 1e-12) -> SparsePauliOp:
    """Decompose a 4x4 Hermitian matrix into a sum of two-qubit Pauli strings."""
    labels = []
    coefficients = []

    for symbols in product("IXYZ", repeat=2):
        label = "".join(symbols)
        pauli_matrix = Pauli(label).to_matrix()
        coefficient = np.trace(pauli_matrix @ matrix) / 4

        if abs(coefficient) > tolerance:
            labels.append(label)
            coefficients.append(np.real_if_close(coefficient))

    return SparsePauliOp(labels, coefficients)
