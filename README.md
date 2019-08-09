# Python-Minisat [![Build Status](https://travis-ci.org/pgdr/python-minisat.svg?branch=master)](https://travis-ci.org/pgdr/python-minisat)

Python bindings around [MiniSat](https://codingnest.com/modern-sat-solvers-fast-neat-underused-part-1-of-n/).


```python
s = minisat.Solver()
x = s.new_var()
y = s.new_var()
c = [minisat.lit(x), minisat.lit(y)]
s.add_clause_vec(c)
assert s.solve()
```

we can also read `DIMACS` format from the terminal:

```bash
$ pyminisat
c An example formula
c
p cnf 3 4
1 2 3 0
-1 2 3 0
1 -2 3 0
1 2 -3 0

True
```

and programmatically:

```python
DIMACS="""
c An example formula
c
p cnf 3 4
1 2 3 0
-1 2 3 0
1 -2 3 0
1 2 -3 0
"""
clauses, summary, vars_, sat_vars, solver = minisat.create_dimacs_solver(DIMACS)
assert summary == ['p cnf 3 4']
assert len(clauses) == 4
assert len(vars_) == 3
assert solver.solve() is True
```

## why

This project is just me learning
* [pybind11](https://pybind11.readthedocs.io/en/stable) [(GitHub)](https://github.com/pybind/pybind11)
* [minisat](https://codingnest.com/modern-sat-solvers-fast-neat-underused-part-1-of-n/) [(GitHub)](https://github.com/master-keying/minisat)
* [scikit-build](https://scikit-build.readthedocs.io/en/latest/) [(GitHub)](https://github.com/scikit-build/scikit-build)
* [manylinux (GitHub)](https://github.com/pypa/manylinux)
* C++, CMake, and not least, some programming
