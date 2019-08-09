from .minisatbind import mklit, var, sign, Solver, lbool


def lit(v, sign=True):
    return mklit(v, sign)


def to_lit(solver_vars, var):
    if var < 0:
        return -lit(solver_vars[abs(var)])
    return lit(solver_vars[abs(var)])


def create_solver(clauses):
    s = Solver()
    solver_vars = {}
    for clause in clauses:
        for c in clause:
            var = abs(c)
            if var not in solver_vars:
                solver_vars[var] = s.new_var()
        vars_ = [to_lit(solver_vars, var) for var in clause]
        s.add_clause(*vars_)
    return s, solver_vars
