#include <pybind11/pybind11.h>
#include <minisat/mtl/Vec.h>
#include <minisat/core/Solver.h>
#include <minisat/core/SolverTypes.h>

namespace py = pybind11;


PYBIND11_MODULE(minisatbind,m) {
    m.doc() = "minisat-to-python bindings";

    py::class_<Minisat::Lit>(m, "Lit")
      .def(py::init<int &>())
      .def("__repr__",
           [](const Minisat::Lit &l) {
             int var = Minisat::var(l);
             auto vars = std::to_string(var);
             int sig = Minisat::sign(l);
             auto sigs = std::to_string(sig);
             return "<Lit var='" + vars + "', sig='"+sigs+"'>";
           })
      .def("__neg__",
           [](const Minisat::Lit &l) {
             return ~l;
           });

    m.def("mklit", &Minisat::mkLit, "Lit mkLit(Var var, bool sign);");
    m.def("var", &Minisat::var, "var(lit)");
    m.def("sign", &Minisat::sign, "sign(lit)");

}
