#!/bin/bash
set -e -x

# Install a system package required by our library
yum install -y centos-release-scl devtoolset-6 rh-python36-python-devel git scl-utils zlib zlib-devel

source /opt/rh/devtoolset-6/enable
source /opt/rh/rh-python36/enable

pip install --upgrade pip
pip install --upgrade cmake setuptools pytest ninja scikit-build


# BUILD MINISAT

git clone https://github.com/pgdr/minisat
pushd minisat
git fetch origin niklasso:niklasso
git checkout niklasso
mkdir build
pushd build
cmake .. -DBUILD_SHARED_LIBS=ON
make -j2 install
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
popd
popd


# BUILD PYTHON-MINISAT

git clone https://github.com/pgdr/python-minisat
pushd python-minisat

pip install -r requirements.txt

pushd /io/
git clone https://github.com/pybind/pybind11
popd


# WHEELS IN THE HOUSE

pip wheel /io/ -w wheelhouse

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    auditwheel repair "$whl" --plat $PLAT -w /io/wheelhouse/
done

pip install minisat --no-index -f /io/wheelhouse
