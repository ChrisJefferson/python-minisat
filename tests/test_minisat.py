import itertools
import minisat


def test_list():
    l = minisat.lit(0)
    assert minisat.var(l) == 0
    assert minisat.sign(l) is True


def test_var():
    s = minisat.Solver()
    x = s.new_var()
    assert x == 0
    y = s.new_var()
    assert y == 1
    z = s.new_var()
    assert z == 2


def _construct_clause(chi):
    def sign(val, c):
        return -val if c == 0 else val

    return [sign(1, chi[0]), sign(2, chi[1]), sign(3, chi[2])]


def test_minisat_sat():
    powerset = itertools.product((0, 1), repeat=3)
    clauses = [_construct_clause(chi) for chi in powerset]
    clauses.remove([-1, 2, -3])

    s, solver_vars = minisat.create_solver(clauses)

    assert s.solve() is True
    assert not s.model_value(solver_vars[1])
    assert s.model_value(solver_vars[2])
    assert not s.model_value(solver_vars[3])


def test_minisat_unsat():
    powerset = itertools.product((0, 1), repeat=3)
    clauses = [_construct_clause(chi) for chi in powerset]

    s, solver_vars = minisat.create_solver(clauses)

    assert s.solve() is False


def test_create_solver():
    clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3]]
    s, solver_vars = minisat.create_solver(clauses)

    assert s.num_vars() == 3
    assert s.num_clauses() == 4

    assert s.solve() is True
    assert not s.model_value(solver_vars[1])
    assert not s.model_value(solver_vars[2])
    assert not s.model_value(solver_vars[3])


def test_add_clause_vec():
    s = minisat.Solver()
    x = s.new_var()
    y = s.new_var()
    c = [minisat.lit(x), minisat.lit(y)]
    ret = s.add_clause_vec(c)

    assert ret
    assert s.num_vars() == 2
    assert s.num_clauses() == 1
    assert s.solve()
