# Python-Minisat [![Build Status](https://travis-ci.org/pgdr/python-minisat.svg?branch=master)](https://travis-ci.org/pgdr/python-minisat)

Python bindings around [MiniSat](https://codingnest.com/modern-sat-solvers-fast-neat-underused-part-1-of-n/).


```python
def test_create_solver():
    clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3]]
    s, solver_vars = minisat.create_solver(clauses)
    assert s.solve() is True
    assert not s.model_value(solver_vars[1])
    assert not s.model_value(solver_vars[2])
    assert not s.model_value(solver_vars[3])
```