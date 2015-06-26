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

"""Generate the digits of Pi using a streaming algorithm.

.. moduleauthor:: Sameer Marathe

"""

from .pidigits_lambert import piGenLambert as piGenerator
from .pidigits_lambert import getPiLambert as getPi
from .pidigits import piGenLeibniz
from .pidigits import getPiLeibniz
from .pidigits_gosper import piGenGosper
from .pidigits_gosper import getPiGosper
from .taudigits import tauGenLeibniz
from .taudigits import getTauLeibniz
from .taudigits_lambert import tauGenLambert as tauGenerator
from .taudigits_lambert import getTauLambert as getTau
