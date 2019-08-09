from skbuild import setup

setup(
    name="minisat",
    packages=["minisat"],
    version="0.0.2",
    author="pgdr",
    url="https://github.com/pgdr/python-minisat",
    install_requires=["scikit-build"],
    tests_require=["pytest"],
)
