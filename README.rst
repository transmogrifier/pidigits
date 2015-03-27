PiDigits
********

*PiDigits* Implements the 'Unbounded Spigot Algorithm for the Digits of Pi' by
Jeremy Gibbons. The paper describing this algorithm can be found at the
following URL: `http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
<http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf>`

Installation
------------
*pidigits* is avalaible through Python Package Index (`PyPI 
<https://pypi.python.org/pypi>`_) using `pip 
<http://www.pip-installer.org/en/latest/index.html>`_. ::

   >>> pip install --upgrade pidigits

To uninstall using `pip
<http://www.pip-installer.org/en/latest/index.html>`_. ::

   >>> pip uninstall pidigits

Usage
-----
PiDigits provides a generator function named *piGenerator* that yields the 
digits of Pi as needed. ::

    >>> from pidigits import piGenerator
    >>> mypi = piGenerator()
    >>> first20pi = [mypi.next() for i in range(20)]
    >>> first20pi
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

*Example*: Verify the `Feynman point 
<http://en.wikipedia.org/wiki/Feynman_point>`. ::

    >>> mypi = piGenerator()
    >>> first1001 = [mypi.next() for i in range(1001)]
    >>> feynman = first1001[762:768]
    >>> print feynman
    [9, 9, 9, 9, 9, 9]

Alternatively you can also use the *getPi(n)* function to get the first *n*
digits of Pi. ::

    >>> from pidigits import getPi
    >>> first20pi = getPi(20)
    >>> first20pi
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]

License
-------
pidigits is licensed under `Apache License 2.0 
<https://www.apache.org/licenses/LICENSE-2.0.html>`_.
