#!/usr/bin/env python3
"""
Math Solver (Local Wolfram Alpha Alternative)
Uses sympy and scipy for symbolic and numerical math.
Handles: Calculus, Algebra, Solving Equations, Units, Simplification.
"""

import sys
import argparse
import re
from sympy import (
    symbols, sympify, solve, diff, integrate, limit, oo, 
    simplify, expand, factor, latex, init_printing, N, 
    sin, cos, tan, log, exp, sqrt, pi, E, Eq
)
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application, 
    convert_xor, function_exponentiation
)

def safe_parse(expr_str, local_dict=None):
    """Safely parse a math expression string into a sympy object."""
    transformations = standard_transformations + (implicit_multiplication_application, convert_xor, function_exponentiation)
    return parse_expr(expr_str, local_dict=local_dict or {}, transformations=transformations)

def solve_math(query):
    """Process a math query and return the result."""
    query = query.strip()
    
    try:
        # 1. Solving Equations (e.g., "solve x**2 - 4 = 0" or "solve for x: 2x + 5 = 15")
        if query.lower().startswith("solve "):
            eq_part = query.replace("solve ", "", 1).replace("for x:", "=").replace("for x =", "=").strip()
            if "=" in eq_part:
                lhs_str, rhs_str = eq_part.split("=", 1)
                lhs = safe_parse(lhs_str)
                rhs = safe_parse(rhs_str)
                x = symbols('x')
                solutions = solve(lhs - rhs, x)
                return f"Solutions: x = {solutions}"
            else:
                # Just solving an expression for roots (e.g., "solve x**2 - 4")
                expr = safe_parse(eq_part)
                x = symbols('x')
                solutions = solve(expr, x)
                return f"Roots: x = {solutions}"

        # 2. Derivatives (e.g., "derivative of x**3 + 2*x wrt x" or "diff x**2")
        elif "derivative" in query.lower() or query.lower().startswith("diff "):
            expr_part = query.replace("derivative of ", "").replace("diff ", "").replace(" wrt x", "").replace(" with respect to x", "").strip()
            expr = safe_parse(expr_part)
            x = symbols('x')
            result = diff(expr, x)
            return f"Derivative: {result}\nLatex: {latex(result)}"

        # 3. Integrals (e.g., "integrate x**2 from 0 to 1" or "integral of x**3")
        elif "integrate" in query.lower() or "integral" in query.lower():
            parts = query.lower().split(" from ")
            expr_part = parts[0].replace("integrate ", "").replace("integral of ", "").strip()
            expr = safe_parse(expr_part)
            x = symbols('x')
            
            if len(parts) > 1:
                bounds = parts[1].strip().split(" to ")
                if len(bounds) == 2:
                    a, b = bounds
                    result = integrate(expr, (x, a, b))
                    return f"Definite Integral: {result}\nNumerical: {float(N(result))}"
            
            result = integrate(expr, x)
            return f"Indefinite Integral: {result}\nLatex: {latex(result)}"

        # 4. Limits (e.g., "limit of 1/x as x -> 0" or "limit sin(x)/x x->0")
        elif "limit" in query.lower():
            # Basic parsing for "limit of [expr] as [var] -> [val]"
            match = re.search(r"limit\s+of\s+(.+?)\s+as\s+(\w+)\s*->\s*(.+)", query, re.IGNORECASE)
            if match:
                expr_str, var, val = match.groups()
                expr = safe_parse(expr_str)
                x = symbols(var)
                if val.strip().lower() in ['oo', 'infinity']:
                    result = limit(expr, x, oo)
                elif val.strip().lower() == '-oo':
                    result = limit(expr, x, -oo)
                else:
                    result = limit(expr, x, val.strip())
                return f"Limit: {result}"
            else:
                return "Error: Could not parse limit. Try 'limit of 1/x as x -> 0'"

        # 5. Simplify / Expand / Factor
        elif query.lower().startswith(("simplify ", "expand ", "factor ")):
            cmd = query.split()[0]
            expr_str = query[len(cmd):].strip()
            expr = safe_parse(expr_str)
            if cmd == "simplify":
                return f"Simplified: {simplify(expr)}"
            elif cmd == "expand":
                return f"Expanded: {expand(expr)}"
            else:
                return f"Factored: {factor(expr)}"

        # 6. General Evaluation (e.g., "sqrt(16) + 2*pi" or "sin(pi/2)")
        else:
            expr = safe_parse(query)
            result = N(expr) # Numerical evaluation
            if result.is_real and not result.is_Float:
                 return f"Exact: {expr}\nNumerical: {result}"
            return f"Result: {result}"

    except Exception as e:
        return f"Error processing math: {str(e)}\nHint: Use standard Python math syntax (e.g., x**2, sin(x), log(x))."

def main():
    parser = argparse.ArgumentParser(description="Local Math Solver (Wolfram Alpha alternative)")
    parser.add_argument("query", help="The math problem to solve")
    parser.add_argument("--latex", action="store_true", help="Output LaTeX format")
    args = parser.parse_args()
    
    result = solve_math(args.query)
    print(result)

if __name__ == "__main__":
    main()
