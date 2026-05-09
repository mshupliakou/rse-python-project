# PhysCalc (phys-engine-cool)

[![Run Tests](https://github.com/mshupliakou/rse-python-project/actions/workflows/tests.yml/badge.svg)](https://github.com/mshupliakou/rse-python-project/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/mshupliakou/rse-python-project/graph/badge.svg?token=KBD5JZJ2QC)](https://codecov.io/github/mshupliakou/rse-python-project)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**PhysCalc** is a high-performance physics simulation package built with Python. It specializes in calculating free fall trajectories considering air resistance.

## Key Features

* **High Performance**: Mathematical engine accelerated by Numba JIT-compilation.
* **Unit Safety**: Integration with Pint ensures physical quantities are handled correctly across different units.
* **Automation**: Full CI/CD pipeline for automated testing, code coverage reporting, and package publishing.
* **Documentation**: Automatically generated API documentation using MkDocs.

## Installation

For local development, clone the repository and install the package in editable mode:

```bash
pip install .