import modulos.modulo

print modulos.modulo.CONS
print modulos.modulo.CONS2

raw_input("\n")

from modulos import modulo

print modulo.CONS
print modulo.CONS2

raw_input("\n")

import modulos.modulo as m

print m.CONS
print m.CONS2

raw_input("\n")

from modulos.modulo import CONS, CONS2

print CONS
print CONS2

raw_input("\n")


import modulos.mod2.mod2

print modulos.mod2.mod2.CONS
print modulos.mod2.mod2.CONS2

raw_input("\n")

from modulos.mod2.mod2 import CONS,CONS2

print CONS
print CONS2

raw_input("\n")

from modulos.modulo import CONS as C, CONS2 as C2
from modulos.mod2.mod2 import CONS as CC, CONS2 as CC2

print C
print C2
print CC
print CC2
