#SLICING in python
#allows access to one or more elements of a sequence
#immutable sequences : tuples, strings, bytes
#mutable sequences: lists, bytearrays
#accessing is allowed in all sequences
print("Slicing allows access to all types of sequences, as well as modify te mutable sequences")
a_tuple = ('a', 1, 2, (3, 4))
a_string = 'immutable'
a_bytes = b'sequence'
a_list = [5, 6, 7, 8, (4, 5)]
a_byte_array = bytearray(b'mutable')
#printing bytes sequence will print byte value of that element
#use sqr bracket after the name of object and the number in it is the index
print("Positive index\n")
print('tuple[0] ->', a_tuple[0])
print('string[1]->', a_string[1])
print('bytes[2] ->', a_bytes[2])
print('list[3]  ->', a_list[3])
print('bytearray[4] ->', a_byte_array[4])
print(end='\n')
#Negative indexes are from the end
print("Negative indexing\n")
print('tuple[-1] ->', a_tuple[-1])
print('string[-2]->', a_string[-2])
print('bytes[-3] ->', a_bytes[-3])
print('list[-4]  ->', a_list[-4])
print('bytearray[-5] ->', a_byte_array[-5])
#Subslices can be accessed with two indexes
print(end='\n')
print('Two Indexes - accessing subslices')
print('a_list[0:2] ->',a_list[0:2])
#start from 0 till but not including 2 index
print('a_list[:2] ->',a_list[:2])
#start from begining
print('a_list[2:5] ->', a_list[2:5])
#beyond the end
print('a_list[2:] ->', a_list[2:])
#all the wy till the end
print('a_list[:] ->', a_list[:])
#copy of entire list
list_ref = a_list
#reference to that object assigned
#if changes are made in list it will reflect in the refence as well
print('a_list is list_ref ->', a_list is list_ref)
list_copy = a_list[:]
#copy of the object created, doesn't refere to the same list
print('a_list is list_copy ->', a_list is list_copy)
#Steps can be taken with a third parameter
print("-" * 30)
print("Third parameter")
#you can specify interval or steps taken between each slice
print('a_list[::2] ->', a_list[::2])
#starting from beg pick every second i.e. every alternate element
print('a_list[1:4:2] ->', a_list[1:4:2])
#starting from index 1 to but not including index 4, pick every alternate
print('a_string[::-1] ->', a_string[::-1])
#string will be reversed
print(end='\n')
print("Additional slices to access leements with sequences")
print('a_list ->', a_list)
print('a_list[4] ->', a_list[4])
print('a_list[4][0] ->', a_list[4][0])
print('a_list[4][1] ->', a_list[4][1])
#Mutable sequenes can be updated with slices
print('a_list ->', a_list)
a_list[0] = 'five'
print('a_list ->', a_list)
a_list[1:4] = [10, 11, 12]
print('a_list ->', a_list)
print(end='\n')
#A slice object can be used in [] for slicing
a_slice = slice(4)
print('a_slice ->', a_slice)
print('a_list[a_slice] ->', a_list[a_slice])
a_slice = slice(1,5)
print('a_slice ->', a_slice)
