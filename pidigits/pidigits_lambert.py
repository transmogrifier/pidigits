# -*- coding: utf-8 -*-
#   Copyright 2015 Sameer Suhas Marathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
#
#
#   Module description
#   ==================
#   Implements the 'Unbounded Spigot Algorithm for the Digits of Pi' by
#   Jeremy Gibbons. The paper describing this algorithm can be found at the
#   following URL:
#   http://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
#
#   This module implements the algorithm outlined in section 6 of the paper
#   using the continued fraction expression for Pi due to Lambert.

def __comp(a, b):
    (q,r,s,t) = a
    (u,v,w,x) = b
    return (q*u+r*w, q*v+r*x, s*u+t*w, s*v+t*x)

def __extr(a, x):
    (q,r,s,t) = a
    return (q*x + r, s*x + t)

def __extr1(a, x):
    (q,r,s,t) = a
    return (q*x + 2*r, s*x + 2*t)
  
def __prod (a, n):
    return (__comp((10,-10*n, 0, 1), a[0]), a[1])

def __safe(b, n):
    x = 5*b[1] - 2
    a = __extr1(b[0],x)
    return n == a[0]//a[1]

def __cons(z,z1):
    return (__comp(z[0],z1), z[1]+1)

def __next(z):
    x = 2*z[1] - 1
    a = __extr(z[0],x)
    return a[0]//a[1]

def __lfts(k):
    return (2*k -1, k*k, 1, 0)

def piGenLambert():
    """A generator function that yields the digits of Pi
    """
    z = ((0,4,1,0),1)
    while True:
        lft = __lfts(z[1])
        n = int(__next(z))
        if __safe(z,n):
            z = __prod(z,n)
            yield n
        else:
            z = __cons(z,lft)

def getPiLambert(n):
    """Returns a list containing first n digits of Pi
    """
    mypi = piGenLambert()
    result = []
    if n > 0:
        result += [next(mypi) for i in range(n)]
    mypi.close()
    return result
