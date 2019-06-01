#Tuple class - fewer methods/ no methods available to chnage existing tuple
#immutable sequence of elements
empty_tuple = tuple()
#tuple() function is a constructor function which creates mepty tuple
print('empty_tuple ->', empty_tuple)
tuple_str = tuple('hello')
tuple_list = tuple([1, 2, [3, 5, 7]])
#tuple func will convert list into tuple
#tuple function will convert only the outer list into a tuple
print('tuple_list ->', tuple_list)
empty_tuple = ()
print('empty_tuple = () ->', empty_tuple)
singleton_tuple = (1,)
#one single element in a tuple
print('singleton_tuple ->', singleton_tuple)
tuple_syntax = (3, 4, 'a', 'b')
print('tuple_syntax ->', tuple_syntax)
print("'a' in tuple_syntax ->",
      'a' in tuple_syntax)
print("1 not in tuple_syntax ->",
      1 not in tuple_syntax)
print('tuple_str ->', tuple_str)
print('min of str ->', min(tuple_str))
print('max of str ->', max(tuple_str))
print('sorted(str) ->', sorted(tuple_str))
print('count of ("o") ->', tuple_str.count("o"))
print('index of ("o") ->', tuple_str.index("o"))
print('index of ("l") ->', tuple_str.index("l"))
print('length of tuple str ->', len(tuple_str))
#no sort or reverse method is available for tuple
