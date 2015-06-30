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

"""
.. module:: pidigits._tests.test_pidigits
    :synopsis: Unittest for pidigits.

.. moduleauthor:: Sameer Marathe

"""

from unittest import TestCase
from pidigits import tauGenerator
from pidigits import tauGenLeibniz
from timeit import default_timer

class TestTauDigits(TestCase):

    @classmethod
    def setUpClass(cls):
        #Setup the first 10000 decimal digits
        starttime = default_timer()
        mytau = tauGenerator()
        #10000 digits after decimal
        cls.first1e4 = [next(mytau) for i in range(10001)]
        mytau.close()
        elapsed = default_timer() - starttime
        print("{0:.3f} seconds to generate 10,000 digits of Tau".
                format(elapsed))

    def test_FeynmanPoint(self):
        feynman = self.first1e4[761:768]
        self.assertEqual(feynman,[9,9,9,9,9,9,9]) #Feynman point

class TestTauDigitsLeibniz(TestCase):

    @classmethod
    def setUpClass(cls):
        #Setup the first 10000 decimal digits
        starttime = default_timer()
        mytau = tauGenLeibniz()
        #10000 digits after decimal
        cls.first1e4 = [next(mytau) for i in range(10001)]
        mytau.close()
        elapsed = default_timer() - starttime
        print("{0:.3f} seconds to generate 10,000 digits of Tau".
                format(elapsed))

    def test_FeynmanPoint(self):
        feynman = self.first1e4[761:768]
        self.assertEqual(feynman,[9,9,9,9,9,9,9]) #Feynman point
