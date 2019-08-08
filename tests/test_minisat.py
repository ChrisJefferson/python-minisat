import minisat

def test_minisat():
    clauses = [ 1, -2, 3 ], [-1, 2, 3], [-1, -2, -3], [1, 2, 3]
    minisat_clauses = [minisat.clause(*c) for c in clauses]
    print('phi =', minisat_clauses)

    s = minisat.Solver()
    assert s.new_var() == 0
    assert s.new_var() == 1

    s.add_clause(minisat.mklit(0,0))
