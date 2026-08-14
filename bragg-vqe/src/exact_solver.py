import numpy as np

from .hamiltonian import bragg_hamiltonian


def eigenspectrum(delta_values, omega: float) -> np.ndarray:
    """Exact eigenvalues of the 3-state Hamiltonian for a sweep of detunings."""
    energies = [np.linalg.eigvalsh(bragg_hamiltonian(delta, omega)) for delta in delta_values]
    return np.array(energies)


def ground_state(delta: float, omega: float):
    """Exact ground-state energy and eigenvector at a single detuning."""
    eigenvalues, eigenvectors = np.linalg.eigh(bragg_hamiltonian(delta, omega))
    return eigenvalues[0], eigenvectors[:, 0]


def ground_state_populations(delta_values, omega: float) -> np.ndarray:
    """Exact ground-state momentum populations for a sweep of detunings."""
    populations = []
    for delta in delta_values:
        _, ground = ground_state(delta, omega)
        populations.append(np.abs(ground) ** 2)
    return np.array(populations)


def minimum_gap(delta_values, omega: float) -> float:
    """Minimum E1 - E0 gap over a window of detunings, used for avoided-crossing analysis."""
    gaps = []
    for delta in delta_values:
        e0, e1, _ = np.linalg.eigvalsh(bragg_hamiltonian(delta, omega))
        gaps.append(e1 - e0)
    return float(np.min(gaps))
