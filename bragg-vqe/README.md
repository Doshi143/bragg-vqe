# Bragg VQE

A small, self-contained quantum simulation of Bragg diffraction in a Bose–Einstein condensate,
using a truncated 3-state momentum-space model and the Variational Quantum Eigensolver (VQE).

See [weekend_plan.md](weekend_plan.md) for the full project plan and physical background.

## Aims

* Derive a physically meaningful 3-state Bragg Hamiltonian in momentum space.
* Benchmark it exactly on a classical computer (eigenvalues, ground-state populations, avoided
  crossings).
* Encode the Hamiltonian onto 2 qubits and verify the encoding reproduces the exact physics.
* Decompose the encoded Hamiltonian into Pauli strings for use as a VQE operator.
* Run VQE with a noise-free statevector estimator and benchmark it against the exact solution.
* Sweep VQE across detuning, warm-starting each point from the previous optimum, and compare
  against the exact model throughout.

## Outputs

Running the notebooks in `notebooks/` in order (01 → 04) produces:

**Figures** (`figures/`)
1. `fig1_exact_eigenspectrum.png` — exact eigenspectrum vs detuning $\delta$
2. `fig2_exact_vqe_energy.png` — exact and VQE ground-state energies vs $\delta$
3. `fig3_exact_vqe_populations.png` — exact and VQE momentum populations vs $\delta$
4. `fig4_min_gap_vs_omega.png` — minimum avoided-crossing gap vs $\Omega$
5. `fig5_momentum_wavefunctions.png` — VQE momentum-space probability density at
   $\delta = -4, 0, 4$
6. `ansatz_circuit.png` — the two-qubit VQE ansatz circuit diagram

**Data** (`results/`)
* `vqe_detuning_sweep.csv` — per-detuning exact/VQE energies, energy error, fidelity, momentum
  populations, and leakage into the unphysical $|11\rangle$ state

**Tables** (printed in `04_detuning_sweep.ipynb` and `03_vqe_single_point.ipynb`)
* energy/fidelity comparison table (exact vs VQE at sample detunings)
* optimizer comparison table (COBYLA, Nelder-Mead, L-BFGS-B, SPSA)

**Verified derivations** (`02_encoding_and_pauli_form.ipynb`)
* the 2-qubit encoding matches the exact 3-state spectrum
* the Pauli decomposition matches the encoded Hamiltonian matrix exactly

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

`src/` holds the reusable physics and VQE code; the notebooks import from it and add the
exploratory/plotting layer on top.

## Theory

*(to be added)*
