import itertools
import minisat


def test_lbool():
    b0 = minisat.lbool(False)
    assert not b0
    b1 = minisat.lbool(True)
    assert b1


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


def _construct_clause(v0, v1, v2, b0, b1, b2):
    l0 = minisat.lit(v0) if b0 else -minisat.lit(v0)
    l1 = minisat.lit(v1) if b1 else -minisat.lit(v1)
    l2 = minisat.lit(v2) if b2 else -minisat.lit(v2)
    return l0, l1, l2


def test_minisat_sat():
    s = minisat.Solver()
    x = s.new_var()
    y = s.new_var()
    z = s.new_var()

    powerset = itertools.product((0, 1), repeat=3)
    for chi in powerset:
        c = _construct_clause(x, y, z, *chi)
        if chi != (0, 0, 0):
            s.add_clause(*c)
    assert s.solve() is True
    assert not s.model_value(x)
    assert not s.model_value(y)
    assert not s.model_value(z)


def test_minisat_unsat():
    s = minisat.Solver()
    x = s.new_var()
    y = s.new_var()
    z = s.new_var()

    powerset = itertools.product((0, 1), repeat=3)
    for chi in powerset:
        c = _construct_clause(x, y, z, *chi)
        s.add_clause(*c)
    assert s.solve() is False
