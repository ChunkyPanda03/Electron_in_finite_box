import sympy
from sympy import *
from sympy.abc import x, y
import multiprocessing as mp


def solve_equation(domain):
    m = 511000
    E = 1
    h_ = (.658) * 10 ** -15
    express1 = sympy.tan(sympy.sqrt((2 * m * E) / (h_ ** 2)) * x)
    express2 = (-sympy.sqrt(E / (x - E)))
    return solve([Eq(express2, express1)], x, domain=domain, particular=True, quick=True)


if __name__ == '__main__':
    pool = mp.Pool(processes=15)
    results = pool.map(solve_equation, [(1, 1.5), (1.5, 2)])
    print(results)

    # Save results to a text file
    with open('results.txt', 'w') as f:
        for i, res in enumerate(results):
            f.write(f'Results for domain {i + 1}: {res}\n')
#optimized with chat gpt