# Vivar-Operator-Spectral-Analysis

## Abstract
This repository provides the computational framework and empirical validation for the **Vivar Operator**, a novel spectral construction designed to map the non-trivial zeros of the Riemann zeta function. Our objective is to demonstrate that the spectral distribution of this operator is isomorphic to the distribution of the zeta zeros, confirming their adherence to the Gaussian Unitary Ensemble (GUE) statistics.



## Research Significance
The Riemann Hypothesis remains the most profound challenge in analytic number theory. Historically, attempts to construct a spectral operator for the zeta function have encountered significant obstacles regarding spectral completeness. This project introduces a verifiable, audit-ready approach based on spectral rigidities and spacing distributions, providing a deterministic foundation for the critical line conjecture.

## Methodology
The validation process utilizes two rigorous statistical metrics:

1. **Nearest Neighbor Spacing Distribution (NNSD):** An analysis of the spacing between consecutive zeros to verify the quantum chaotic nature of the system.
2. **Dyson-Mehta Delta_3 Statistic:** A measurement of long-range spectral rigidity, demonstrating that the zeros of the Vivar Operator exhibit the same logarithmic growth patterns characteristic of the GUE, effectively ruling out Poisson-like randomness.



## Contents
* /src: Contains the primary auditing scripts (nnsd_auditor.py and rigidity_auditor.py).
* /results: Datasets and output logs from the audit of the first 500 non-trivial zeros.

## Usage
The scripts are implemented in Python 3, utilizing the mpmath library for high-precision arbitrary-length arithmetic (set to 40 decimal places for spectral fidelity).

### Prerequisites
Ensure you have the following libraries installed:
- numpy
- mpmath

### Execution
To replicate the spectral analysis, navigate to the root directory and execute:

python3 src/nnsd_auditor.py
python3 src/rigidity_auditor.py

## Reproducibility
This repository is intended as an open audit-lab. We invite the mathematical community to perform independent verification of the results presented herein, reinforcing the paradigm that fundamental truths in number theory must be inherently verifiable and reproducible.

