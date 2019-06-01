#COLLECTIONS AND MAPPINGS
#1. RANGE FUNCTION
print('"Range" Function Demo')
a = range(5)
print('a range ->', a) #generates integers
print('list(a) ->', list(a)) #generates list of those integers
print('Can be used in a for loop')
for i in range(5):
    print(i, end=' ') #executed 5 times
    print(' ')
print()
print('Can be used like slice function '
      'with a start, stop and step')
a_range = range(10) #stop only
print('list(a_range) ->', list(a_range))
a_range = range(10, 16) #start and stop
print('list(a_range) ->', list(a_range))
a_range = range(10, -1, -1) #start, stop and step
print('list(a_range) ->', list(a_range))
a_range = range(10, -1, -2) #start, stop and step
print('list(a_range) ->', list(a_range))
print('_' * 40)
#2. SET CLASS
print('Set class allows to create unique immutable elements')
empty_set = set() #set constructor by default is empty set
print('empty_set ->', empty_set)
alpha = set(('a', 'b', 'c', 'd')) #unordered list {}
print('set alpha :', alpha)
#duplicate lists - to eliminate duplicates using sets
dup = ['c', 'd', 'c', 'd', 'e', 'f']
beta = set(dup)
print('set beta :', beta)
uniquelist = list(beta)
print('unique list :', uniquelist)
#UNION/ OR: combination with duplicates removed
gamma = alpha.union(beta)
print('set gamma :', gamma)
gamma = alpha | beta
print('gamma :', gamma)
#Intersect/ AND: common/ overlap
delta = alpha.intersection(beta)
print('set delta :', delta)
delta = alpha & beta
print('delta :', delta)
#Difference: only present in alpha
epsilon = alpha.difference(beta)
print('epsilon :', epsilon)
epsilon = alpha - beta
print('epsilon :', epsilon)
#XOR/ Union - intersection: all elements except the overlapping elements
eta = alpha.symmetric_difference(beta)
print('eta :', eta)
eta = alpha ^ beta
print('eta :', eta)
#to see if two sets share any elements
print('epsilon.isdisjoint(delta) :', epsilon.isdisjoint(delta))
print('epsilon.isdisjoint(eta) :', epsilon.isdisjoint(eta))
#subset
print('epsilon.issubset(eta) :', epsilon.issubset(eta))
print('epsilon.issubset(beta):', epsilon.issubset(beta))
#superset
print('eta.issuperset(epsilon) :', eta.issuperset(epsilon))
print('beta.issuperset(epsilon):', beta.issuperset(epsilon))
#Frozen sets are immutable
feta = frozenset(eta)
print('feta :', feta)
#things that only apply to sets not frozen sets
zeta = set()
print('zeta :', zeta)
zeta.add(3)
#elements added have to be unique
print('zeta :', zeta)
zeta.add(3) #added again will still show once
print('zeta :', zeta)
zeta.add(4)
print('zeta :', zeta)
print('gamma :', gamma)
gamma.discard('a') #if element is present will be removed
print('gamma :', gamma)
gamma.discard('z') #if element is not present it will be ignored no error
print('gamma :', gamma)
gamma.remove('b')
print('gamma :', gamma)
random_element = gamma.pop()
#random element will be popped out
print('random_element pop :', random_element)
print('gamma :', gamma)
print(' ')
print('creating reference to a set')
zeta_ref = zeta
zeta_copy = zeta.copy()
zeta.clear() #any changes to original will reflect on reference but not on copy
print('zeta :', zeta)
print('zeta_ref :', zeta_ref)
print('zeta_copy :', zeta_copy)
#update()
print('alpha :', alpha)
alpha_diff = alpha.copy()
alpha_diff.difference_update(beta)
print('alpha_diff :', alpha_diff)
#
alpha_intersect = alpha.copy()
alpha_intersect.intersection_update(beta)
print('alpha_intersect :', alpha_intersect)
#
alpha_sym_diff = alpha.copy()
alpha_sym_diff.symmetric_difference_update(beta)
print('alpha_sym_diff :', alpha_sym_diff)
#
alpha_union = alpha.copy()
alpha_union.update(beta)
print('alpha_union :', alpha_union)
