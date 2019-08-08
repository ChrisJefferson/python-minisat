from .minisatbind import mklit, var, sign, Solver, lbool


def lit(v, sign=True):
    return mklit(v, sign)
