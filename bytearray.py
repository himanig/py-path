#bytearray
mepty_array = bytearray()
null_array = bytearray(11)
#null array with an integer value means there will be filled with nulls. there iwll be 11 elements initialised with byte value of 0 or null
ints_array = bytearray((84, 114, 97, 100, 22, 174))
#str_array = bytearray('str', 'encoding')
str_array = bytearray('Trademark ®', 'utf-8')
bytes_array = bytearray(b'Trademark \xc2\xae')
print('bytes_array =', bytes_array)
print('bytes_array.decode() -->', bytes_array.decode())
str_literal = 'Trademark ®'
#
print('count(T) -->', str_literal.count('T'))
print('index(T) -->', str_literal.index('T'))
print(end='\n')
print('by byte value :')
print('count(0x54) -->', bytes_array.count(0x54))
print('index(0x54) -->', bytes_array.index(0x54))
#bytearray objects have methods to mutate them or ability to change them with methods
#i.e. add on or remove elements from the array
#byte value 32 represents a space
#0x54 hexadecimal 54 is capital t
#pop method with remove
bytes_array.append(32)
print('append/ add a space at the end')
print(bytes_array)
bytes_array.extend((194, 174))
#extend the array
print('after extend :', bytes_array)
print('_' * 40)
print('bytes_array.decode() :', bytes_array.decode())
bytes_array.remove(0x54)
print('after remove :', bytes_array)
bytes_array.insert(0, 0x54)
print('after insert at position 0 :', bytes_array)
print('after insert at position 0 :', bytes_array.decode())
bytes_array.pop()
print('after first pop: ', bytes_array)
bytes_array.pop()
print('after second pop: ', bytes_array.decode())

