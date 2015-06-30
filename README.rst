PiDigits
********

*PiDigits* Implements the 'Unbounded Spigot Algorithm for the Digits of Pi' by
Jeremy Gibbons. The paper describing this algorithm can be found at this
`URL`_. The same algorithm is used to generate digits of `Tau`_. No matter which
circle constant you prefer, you can now generate the decimal expansion using
this package.

Installation
------------
*pidigits* is avalaible through Python Package Index (`PyPI`_) using `pip`_. ::

   >>> pip install --upgrade pidigits

To uninstall using `pip`_. ::

   >>> pip uninstall pidigits

Usage
-----
PiDigits provides a generator function named *piGenerator* that yields the
digits of Pi as needed. The streaming algorithm based on Lambert's expression
is used for the generator function. ::

    >>> from pidigits import piGenerator
    >>> mypi = piGenerator()
    >>> first20pi = [next(mypi) for i in range(20)]
    >>> first20pi
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

**Example**: Verify the `Feynman point`_. ::

    >>> mypi = piGenerator()
    >>> first1001 = [next(mypi) for i in range(1001)]
    >>> feynman = first1001[762:768]
    >>> print feynman
    [9, 9, 9, 9, 9, 9]

Alternatively you can also use the *getPi(n)* function to get the first *n*
digits of Pi. ::

    >>> from pidigits import getPi
    >>> first20pi = getPi(20)
    >>> first20pi
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

Alternate implementations of streaming algorithms based on Leibniz series and
Gosper's series are also available as generator functions *piGenLeibniz* and
*piGenGosper* and corresponding *getPiLeibniz* and *getPiGosper* functions.
These implementations are slower than the one based on Lambert's series.

Pidigits also provides a generator function name *tauGenerator* that yields the
digits of `Tau`_ as needed. ::

    >>> from pidigits import tauGenerator
    >>> mytau = tauGenerator()
    >>> first20tau = [next(mytau) for i in range(20)]
    >>> first20tau
    [6, 2, 8, 3, 1, 8, 5, 3, 0, 7, 1, 7, 9, 5, 8, 6, 4, 7, 6, 9]

Alternatively you can also use the *getTau(n)* function to get the first *n*
digits of Tau.

Development
-----------
If you clone the repository (`GitHub`_, `BitBucket`_) and make any changes to
the algorithm you can run the test cases in the _tests package included with
the source to test your changes.

To run the tests, in the same directory as *setup.py*, first run: ::

    >>> python setup.py develop

This will install the package in the 'development' mode. Then run the
test cases: ::

    >>> python setup.py test

`Bug reports`_ or suggestions are most welcome.

License
-------
pidigits is licensed under `Apache License 2.0`_.

.. _URL: http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
.. _PyPI: https://pypi.python.org/pypi
.. _pip: https://pip.pypa.io
.. _Apache License 2.0: https://www.apache.org/licenses/LICENSE-2.0.html
.. _Feynman point: http://en.wikipedia.org/wiki/Feynman_point
.. _GitHub: https://github.com/transmogrifier/pidigits
.. _BitBucket: https://bitbucket.org/transmogrifier/pidigits
.. _Bug reports: https://github.com/transmogrifier/pidigits/issues
.. _Tau: https://tauday.com/tau-manifesto
