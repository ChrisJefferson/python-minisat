from .minisatbind import mklit, var, sign, Solver

def lit(v, sign=True):
    return mklit(v, sign)

def clause(v1, v2, v3):
    return [lit(abs(x), sign=(x<0)) for x in (v1, v2, v3)]
