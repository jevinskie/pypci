from setuptools import setup

setup(
    name="pypci",
    description="cffi-based libpci wrapper for python",
    license="MIT",
    version="0.1",
    author='gwangyi',
    maintainer='gwangyi',
    author_email='gwangyi.kr@gmail.com',
    packages=['pypci'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
    ],
    setup_requires=[
        'cffi>=1.0.0',
        'pycparserlibc @ git+https://github.com/gwangyi/pycparserlibc',
        'cffi_ext @ git+https://github.com/gwangyi/cffi_ext',
    ],
    cffi_modules=['build.py:ffi_builder'],
    install_requires=[
        'cffi>=1.0.0',

    ],
)
