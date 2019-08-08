from .minisatbind import mklit, var, sign, Solver

def lit(v, sign=True):
    return mklit(v, sign)
