#include <stdexcept>
#include <map>
#include <pybind11/pybind11.h>
#include <minisat/core/Solver.h>
#include <minisat/core/SolverTypes.h>

namespace py = pybind11;

bool solve(py::list clauses) {
  Minisat::Solver solver;
  std::map<Minisat::Var, Minisat::Var> vars;

  for (int i = 0; i < py::len(clauses); ++i) {
    py::list clause = clauses[i].cast<py::list>();
    auto literal = clause[0].cast<Minisat::Lit>();

    auto x = Minisat::var(literal);
    if (vars.find(x) == vars.end()) {
      vars.insert(std::make_pair(x, solver.newVar()));
    }
    auto var = vars.find(x)->second;
    if (Minisat::sign(literal))
      solver.addClause(Minisat::mkLit(var));
    else
      solver.addClause(~Minisat::mkLit(var));
  }

  return solver.solve();
}


PYBIND11_MODULE(minisatbind,m) {
    m.doc() = "minisat-to-python bindings";

    py::class_<Minisat::Lit>(m, "Lit")
      .def(py::init<int &>())
      .def("__repr__",
           [](const Minisat::Lit &l) {
             auto var = "x_{" + std::to_string(Minisat::var(l)) + "}";
             if (Minisat::sign(l))
               return "~" + var;
             return var;
           })
      .def("__neg__",
           [](const Minisat::Lit &l) {
             return ~l;
           });

    m.def("mklit", &Minisat::mkLit, "Lit mkLit(Var var, bool sign);");
    m.def("var", &Minisat::var, "var(lit)");
    m.def("sign", &Minisat::sign, "sign(lit)");

    m.def("solve", &solve, "solve([ [a,b,c], [-a,c,-d]])");
}
