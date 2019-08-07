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
             return "<Lit x='" + std::to_string(l.x) + "'>";
           })
           ;

    m.def("lit", &Minisat::toLit, "");

}
