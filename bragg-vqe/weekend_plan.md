# Weekend Project Plan: VQE for Bragg Diffraction

## Aim

This weekend version of the project builds a small, self-contained quantum simulation of Bragg
diffraction in a Bose–Einstein condensate using a truncated momentum-space model and the
Variational Quantum Eigensolver (VQE).

The goal is not to solve the full interacting Gross-Pitaevskii equation. The goal is to:

1. derive a physically meaningful 3-state Bragg Hamiltonian,
2. benchmark it exactly on a classical computer,
3. encode it on 2 qubits,
4. run VQE on the encoded Hamiltonian,
5. compare VQE against exact results across detuning.

This keeps the project compact enough for a weekend while still being physically motivated and
CV-worthy.

## Physical model

The model starts from a moving optical lattice potential of the form

$$
V(x,t)=V_0\cos(2k_Lx-\delta t).
$$

In momentum space, this couples neighboring momentum orders in steps of $2\hbar k_L$. Truncating
to the three most relevant momentum states gives the basis

$$
\{|{-1}\rangle, |0\rangle, |{+1}\rangle\}.
$$

The resulting Hamiltonian is

$$
H=\begin{pmatrix}
4+\delta & \Omega & 0\\
\Omega & 0 & \Omega\\
0 & \Omega & 4-\delta
\end{pmatrix}
$$

in dimensionless units, where $\Omega$ is the lattice coupling strength and $\delta$ is the
detuning.

## What will be implemented

### 1. Exact classical model

* Build the 3-state Hamiltonian.
* Diagonalize it with NumPy.
* Plot the eigenvalues versus detuning.
* Plot the ground-state momentum populations versus detuning.
* Identify the avoided crossings near $\delta=\pm 4$.

### 2. Two-qubit encoding

* Map the three physical states into the 4 computational basis states of two qubits:
  * $|{-1}\rangle \to |00\rangle$
  * $|0\rangle \to |01\rangle$
  * $|{+1}\rangle \to |10\rangle$
  * $|11\rangle$ unused
* Add a penalty energy to $|11\rangle$ so VQE avoids the unphysical state.
* Verify that the encoded 4x4 Hamiltonian reproduces the original 3-state physics.

### 3. Pauli decomposition

* Rewrite the 4x4 Hamiltonian as a sum of Pauli strings.
* Check that the Pauli-form operator matches the matrix exactly.
* Use this operator as the input to VQE.

### 4. VQE ground-state search

* Build a small 2-qubit ansatz with a few rotation gates and one entangling gate.
* Use a statevector estimator first, so the calculation is noise-free.
* Minimize the Hamiltonian expectation value with a classical optimizer.
* Compare VQE energy against the exact ground-state energy.
* Compare the VQE state against the exact state using fidelity.

### 5. Detuning sweep

* Run the VQE for a range of detunings.
* Use a random initial point for the first detuning.
* Use the previous optimum as the starting point for the next detuning.
* Store energies, fidelities, momentum populations, and leakage into $|11\rangle$.
* Produce summary plots.

## Project structure

```
bragg-vqe/
├── README.md
├── weekend_plan.md
├── notebooks/
│   ├── 01_exact_model.ipynb
│   ├── 02_encoding_and_pauli_form.ipynb
│   ├── 03_vqe_single_point.ipynb
│   └── 04_detuning_sweep.ipynb
├── src/
│   ├── hamiltonian.py
│   ├── encoding.py
│   ├── exact_solver.py
│   └── vqe_solver.py
├── results/
└── figures/
```

This structure keeps the work organized without making it too heavy.

## Deliverables by the end of the weekend

By the end of the weekend, the project should contain:

* a working 3-state Bragg Hamiltonian,
* exact diagonalization results,
* a correct 2-qubit encoding,
* a verified Pauli decomposition,
* a working VQE implementation,
* exact vs VQE energy comparison,
* exact vs VQE fidelity comparison,
* detuning-sweep plots showing the avoided crossings.

## What is intentionally left out

The weekend version will not include:

* the full nonlinear Gross-Pitaevskii interaction term,
* a larger momentum basis unless there is extra time,
* shot-noise studies,
* hardware runs on a real quantum computer,
* self-consistent mean-field updates.

Those are all good extensions, but they are not needed for the core version.

## Why this version is worth doing

This project is strong because it connects:

* a real cold-atom physics problem,
* a momentum-space truncation that is easy to validate,
* a clean qubit encoding,
* and a practical VQE workflow.

It is small enough to finish, but still physically meaningful and presentable as a portfolio
project.
