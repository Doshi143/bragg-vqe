import numpy as np
from qiskit.circuit import ParameterVector, QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import Statevector, SparsePauliOp
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA, Optimizer


def make_ansatz() -> QuantumCircuit:
    """Two-qubit hardware-efficient ansatz: RY layer, one CX, RY layer."""
    theta = ParameterVector("theta", 4)

    circuit = QuantumCircuit(2)
    circuit.ry(theta[0], 0)
    circuit.ry(theta[1], 1)
    circuit.cx(0, 1)
    circuit.ry(theta[2], 0)
    circuit.ry(theta[3], 1)

    return circuit


def run_vqe(
    hamiltonian: SparsePauliOp,
    optimizer: Optimizer = None,
    initial_point: np.ndarray = None,
):
    """Run VQE with a statevector estimator on the two-qubit ansatz.

    Returns the qiskit_algorithms VQEResult and the resulting statevector amplitudes.
    """
    ansatz = make_ansatz()
    estimator = StatevectorEstimator()
    optimizer = optimizer or COBYLA(maxiter=500)

    vqe = VQE(
        estimator=estimator,
        ansatz=ansatz,
        optimizer=optimizer,
        initial_point=initial_point,
    )
    result = vqe.compute_minimum_eigenvalue(hamiltonian)

    optimal_circuit = ansatz.assign_parameters(result.optimal_parameters)
    state = Statevector.from_instruction(optimal_circuit).data

    return result, state
