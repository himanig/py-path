#List class - allows you to create a mutable sequence of elements
empty_list = list()
print('emty list ->', empty_list)
str_list = list('string')
print('str_list ->', str_list)
tup_list = list((1, 2, (3, 5, 7,)))
#3,5,7 is a tupple inside the other tupple 1,2 containing 3,5,7
print('list tupple ->', tup_list)
#another way to create empty list
empty_list = []
print('emty list ->', empty_list)
#list syntax
list_syn = [3, 4, 'a', 'b']
print('list syn ->', list_syn)
print("'a' in list syn ->", 'a' in list_syn)
print("'4' not in list syn ->", 4 not in list_syn)
print("'1' not in list syn ->", 1 not in list_syn)
empty_list.append(5)
#append extend insert pop remove clear are used to modify a list
#makes it unique to a tupple
print('after append empty list ->', empty_list)
#append one list to another
empty_list.append([6,7])
print('append another list to empty list ->', empty_list)
last_element = empty_list.pop()
print('-' * 40)
print('pop last element ->', last_element)
print('list after pop 1 ->', empty_list)
#extend method
#when you want to add elements of one list to another but not create a list within a list
empty_list.extend([6,7])
print('extend empty list: ', empty_list) 
first_el = empty_list.pop(0)
print(end='\n')
print('pop first element or 0position:', first_el)
print('list after pop(0)', empty_list)
print(end='\n')
empty_list.insert(0, 10)
print('insert at pos 0: ', empty_list)
empty_list.insert(3,100)
print('insert at pos 3: ', empty_list)
#pop works with index
#remove works with value
empty_list.remove(7)
print('remove 7 from list: ', empty_list)
empty_list.clear()
print('list after clear() method ->', empty_list)
print(end='\n')
print('-' * 20)
#operations on string list
print('str list ->', str_list)
print('min of list ->', min(str_list))
print('max of list ->', max(str_list))
print('sorted list ->', sorted(str_list))
#sorted function creates only a copy, doesn't change the original string
print('str_list ->', str_list)
#sort method will change the original string
str_list.sort()
print('using sort() ->', str_list)
str_list.reverse()
print('using reverse() ->', str_list)
print('list str count("r") ->', str_list.count('r'))
print('list str index("r") ->', str_list.index('r'))
print('length of list str ->', len(str_list))
