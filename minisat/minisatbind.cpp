#include <stdexcept>
#include <map>
#include <pybind11/pybind11.h>
#include <minisat/core/Solver.h>
#include <minisat/core/SolverTypes.h>

namespace py = pybind11;


PYBIND11_MODULE(minisatbind,m) {
    m.doc() = "minisat-to-python bindings";

    py::class_<Minisat::lbool>(m, "lbool")
      .def(py::init<bool &>())
      .def("__nonzero__", &Minisat::lbool::isTrue)
      .def("__bool__", &Minisat::lbool::isTrue)
      .def("__repr__",
           [](const Minisat::lbool &b) {
             if (b.isTrue())
               return "<lbool True>";
             return "<lbool False>";
           });

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


    py::class_<Minisat::Solver>(m, "Solver")
      .def(py::init<>())
      .def("new_var", [](Minisat::Solver &s) {
                        bool polarity = true;
                        bool dvar = true;
                        return s.newVar(polarity, dvar);})
      .def("add_clause",
           [](Minisat::Solver &s,
              Minisat::Lit l1,
              Minisat::Lit l2,
              Minisat::Lit l3) {
             return s.addClause(l1, l2, l3);}
        )
      .def("solve", [](Minisat::Solver &s) {
                      return s.solve();
                    })
      .def("model_value",
           [](Minisat::Solver &s,
              Minisat::Var v) {
             return s.modelValue(v);
           }
        );

    m.def("mklit", &Minisat::mkLit, "Lit mkLit(Var var, bool sign);");
    m.def("var", &Minisat::var, "var(lit)");
    m.def("sign", &Minisat::sign, "sign(lit)");
}
