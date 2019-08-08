import minisat

def test_minisat():
    clauses = [ 1, -2, 3 ], [-1, 2, 3], [-1, -2, -3], [1, 2, 3]
    minisat_clauses = [minisat.clause(*c) for c in clauses]
    print('phi =', minisat_clauses)

    assert minisat.solve(minisat_clauses)
