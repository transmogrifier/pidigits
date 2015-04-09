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
from pidigits import piGenerator
from timeit import default_timer

class TestPiDigits(TestCase): 

    @classmethod    
    def setUpClass(cls):
        #Setup the first 10000 decimal digits
        starttime = default_timer()
        mypi = piGenerator()
        #10000 digits after decimal
        cls.first1e4 = [next(mypi) for i in range(10001)]
        mypi.close()
        elapsed = default_timer() - starttime
        print("{0:.3f} seconds to generate 10,000 digits of Pi".
                format(elapsed))
    
    def test_FeynmanPoint(self):
        feynman = self.first1e4[762:768]
        self.assertEqual(feynman,[9,9,9,9,9,9]) #Feynman point
    
    def test_Last10Digits(self):
        #Last 10 digits
        self.assertEqual(self.first1e4[-11:-1],[5,5,2,5,6,3,7,5,6,7])
        
    def test_666(self):
        #From OEIS A083625
        #Occurence of 666
        self.assertEqual(self.first1e4[2440:2443],[6,6,6])
    
    def test_Count1s(self):
        #Test number of 1s
        #From OEIS A099292
        count1 = sum(1 for n in self.first1e4 if n == 1)
        self.assertEqual(count1,1026)
    
    def test_Count3s(self):
        #Test number of 3s
        #From OEIS A099294
        count3 = sum(1 for n in self.first1e4 if n == 3)
        self.assertEqual(count3,975)
    
