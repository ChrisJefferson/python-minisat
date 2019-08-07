cmake_minimum_required(VERSION 3.11.0)
project(cminisat)
find_package(PythonExtensions REQUIRED)

find_package(MiniSat 2.2 REQUIRED)

add_subdirectory(pybind11)
pybind11_add_module(minisatbind minisat/minisatbind.cpp)
target_link_libraries(minisatbind PRIVATE MiniSat::libminisat)

install(TARGETS minisatbind LIBRARY DESTINATION minisat)
