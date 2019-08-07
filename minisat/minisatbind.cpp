#include <pybind11/pybind11.h>
#include <minisat/core/Solver.h>

bool solve() {
    Minisat::Solver solver;
    auto x = Minisat::mkLit(solver.newVar());

    solver.addClause( x);
    solver.addClause(~x);

    return solver.solve();
}


PYBIND11_MODULE(minisatbind,m) {
    m.doc() = "minisat-to-python bindings";
    m.def("solve", &solve, "no args");
}
