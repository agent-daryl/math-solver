# Math Solver — Local Wolfram Alpha Alternative

Free, offline symbolic and numerical math solver using `sympy` and `scipy`.

## Requirements
- Python 3.9+
- `sympy` (pip install sympy)
- `scipy` (pip install scipy)

## Usage

```bash
# Calculus
python3 math_solver.py "integrate x**2 from 0 to 1"
# Result: 1/3 (0.333...)

# Equation Solving
python3 math_solver.py "solve x**2 - 4 = 0"
# Result: x = [-2, 2]

# Derivatives
python3 math_solver.py "derivative of x**3 + 2*x wrt x"
# Result: 3*x**2 + 2

# Limits
python3 math_solver.py "limit of 1/x as x -> 0"

# Simplification
python3 math_solver.py "simplify (x**2 - 1) / (x - 1)"

# General Evaluation
python3 math_solver.py "sqrt(16) + 2*pi"
```

## Supported Operations
| Command | Example |
|---|---|
| Solve Equations | `solve x**2 - 4 = 0` |
| Derivatives | `derivative of x**3 + 2*x wrt x` |
| Integrals | `integrate x**2 from 0 to 1` |
| Limits | `limit of sin(x)/x as x -> 0` |
| Simplify | `simplify (x**2 - 1) / (x - 1)` |
| Expand | `expand (x + 1)**3` |
| Factor | `factor x**2 - 4` |

## Syntax
Uses standard Python/SymPy math syntax:
- Powers: `x**2`
- Functions: `sin(x)`, `cos(x)`, `log(x)`, `exp(x)`, `sqrt(x)`
- Constants: `pi`, `E`
