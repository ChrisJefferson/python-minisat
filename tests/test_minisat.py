import minisat

def test_minisat():
    s = minisat.Solver()
    x = s.new_var()
    y = s.new_var()
    z = s.new_var()

    c1 = (minisat.lit(x),
          minisat.lit(y),
          minisat.lit(z))
    c2 = (-minisat.lit(x),
          minisat.lit(y),
          minisat.lit(z))
    c3 = (minisat.lit(x),
          -minisat.lit(y),
          minisat.lit(z))
    c4 = (minisat.lit(x),
          minisat.lit(y),
          -minisat.lit(z))
    c5 = (-minisat.lit(x),
          -minisat.lit(y),
          minisat.lit(z))
    c6 = (-minisat.lit(x),
          minisat.lit(y),
          -minisat.lit(z))
    c7 = (minisat.lit(x),
          -minisat.lit(y),
          -minisat.lit(z))
    c8 = (-minisat.lit(x),
          -minisat.lit(y),
          -minisat.lit(z))
    s.add_clause(*c1)
    s.add_clause(*c2)
    s.add_clause(*c3)
    s.add_clause(*c4)
    s.add_clause(*c5)
    s.add_clause(*c6)
    s.add_clause(*c7)
    assert s.solve() is True
    s.add_clause(*c8)
    assert s.solve() is False
