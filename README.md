# Central Limit Theorem Simulation

A production-ready Python package for simulating and visualizing the Central Limit Theorem with various probability distributions.

## Features

- 🎲 Simulate the Central Limit Theorem with multiple distributions (Uniform, Exponential, Binomial)
- 📊 Comprehensive statistical analysis of simulation results
- 🎯 Reproducible simulations with seed support
- ✅ Full test coverage
- 📚 Type-safe with Python type hints
- 🚀 Production-ready code with pre-commit hooks and CI/CD ready

## Installation

### Using UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/central-limit-theorem-simulation.git
cd central-limit-theorem-simulation

# Install with UV
uv sync
```

### Using pip

```bash
pip install central-limit-theorem-simulation
```

## Quick Start

### As a Library

```python
from central_limit_theorem_simulation import CentralLimitTheoremSimulator

# Create simulator
simulator = CentralLimitTheoremSimulator(seed=42)

# Simulate uniform distribution
means = simulator.simulate_uniform(n_samples=1000, sample_size=30)

# Get statistics
print(f"Mean: {means.mean():.4f}")
print(f"Std Dev: {means.std():.4f}")
```

### Via Command Line

```bash
# Simulate uniform distribution
clt-sim --seed 42 --n-samples 1000 uniform

# Simulate exponential distribution
clt-sim exponential --sample-size 50

# Simulate binomial distribution
clt-sim binomial --n-samples 500
```

## Development

### Setup Development Environment

```bash
# Install dependencies (including dev dependencies)
uv sync --all-extras

# Run tests
pytest

# Run tests with coverage
pytest --cov

# Run linting and formatting
black src/ tests/
ruff check src/ tests/
mypy src/

# Setup pre-commit hooks
pre-commit install
pre-commit run --all-files
```

### Project Structure

```
central-limit-theorem-simulation/
├── src/
│   └── central_limit_theorem_simulation/
│       ├── __init__.py          # Package exports
│       ├── simulator.py         # Main simulator implementation
│       └── cli.py              # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_simulator.py       # Unit tests
├── docs/                        # Documentation directory
├── .github/
│   └── workflows/              # CI/CD workflows
├── pyproject.toml              # Project configuration
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
├── LICENSE                     # MIT License
└── CONTRIBUTING.md             # Contributing guidelines
```

## Dependencies

### Core Dependencies
- `numpy>=1.24.0` - Numerical computing
- `matplotlib>=3.7.0` - Visualization
- `scipy>=1.10.0` - Scientific computing

### Development Dependencies
- `pytest>=7.0` - Testing framework
- `pytest-cov>=4.0` - Code coverage
- `black>=23.0` - Code formatter
- `ruff>=0.1.0` - Linter
- `mypy>=1.0` - Static type checker
- `pre-commit>=3.0` - Git hooks framework

## Configuration

### Python Versions

This package supports Python 3.10+ and is tested on:
- Python 3.10
- Python 3.11
- Python 3.12

### Code Quality Tools

- **Black**: Line length of 100 characters
- **Ruff**: Configured for multiple rule sets (E, W, F, I, C, B)
- **MyPy**: Type checking enabled
- **Pytest**: 100% test coverage target

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_simulator.py

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=src/central_limit_theorem_simulation --cov-report=html
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this simulator in your research, please cite:

```bibtex
@software{clt_simulation_2024,
  title = {Central Limit Theorem Simulation},
  author = {Your Name},
  year = {2024},
  url = {https://github.com/yourusername/central-limit-theorem-simulation}
}
```

## Support

For support, please open an issue on [GitHub Issues](https://github.com/yourusername/central-limit-theorem-simulation/issues).

## Acknowledgments

Built with modern Python tooling:
- [UV](https://github.com/astral-sh/uv) - Python package manager
- [Pytest](https://pytest.org/) - Testing framework
- [Black](https://github.com/psf/black) - Code formatter
- [Ruff](https://github.com/astral-sh/ruff) - Python linter
