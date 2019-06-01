#comment
#import/using modules
print('List of objects in __main__ namespace: ')
print(dir())
import math
print('List after "import math" is executed')
print(dir())
print('pi = ', math.pi)
print('tan(1) = ',math.tan(1))
del(math)
print(end='\n')
print('List after math is deleted from main:')
print(dir())

#use aliased name for math
import math as m
print('List after math "imported as m" is executed')
print(dir())
print('pi=', m.pi)
print('tan(1)=', m.tan(1))
del(m)
print(end='\n')
print('List after m is deleted from main:')
print(dir())

#import selectively into __main__
from math import pi as p, tan as t
print(end='\n')
print('List after import is executed')
print(dir())
print('pi=', p)
print('tan(1)=', t(1))
del(p,t)
print(end='\n')
print('List after module is deleted from main:')
print(dir())
# i.e. from math import pi,tan
#import selectively with aliases
#from math import pi as pie, tan as tangent
#use wildcard import --> from math import *
from math import *
print(end='\n')
print('list of modules * in math')
print(dir())


