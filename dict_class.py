#DICTIONARY CLASS allows creating associative array of keys and values
#create dictionary object
#keys used have to be unique immutable objects
#dic_syntax = {'key1': 'value1', 'k2': 'v2'}
#dic_syntax2 = dict(k1='v1', k2='v2')
empty_dict = dict()
print('empty_dict ->', empty_dict)
empty_dict = {}
print('empty_dict ->', empty_dict)
d_syntax1 = {'k1': 'v1', 'k2': 'v2'}
print('d_syntax1 ->', d_syntax1)
d_syntax2 = dict(k3='v3', k4='v4')
print('d_syntax2 ->', d_syntax2)
print("d_syntax1['k2'] ->", d_syntax1['k2'])
#to add element to an existing dictionary
d_syntax1['k5'] = 'v5'
print('d_syntax1 ->', d_syntax1) #dictionaries are not normally ordered
del(d_syntax1['k5'])
print('d_syntax1 ->', d_syntax1)
d_syntax1['k1']=1
print('d_syntax1 ->', d_syntax1)
d_syntax1['k2']=2 #keys must be unique values can be same
print('d_syntax1 ->', d_syntax1)
#dictionary reference
dict_ref = d_syntax1
dict_copy = d_syntax1.copy()
d_syntax1.clear()
print('d_syntax1 ->', d_syntax1)
print('dict_ref ->', dict_ref)
print('dict_copy ->', dict_copy)
#methods
key_list = dict_copy.keys()
value_list = dict_copy.values()
print('key_list ->', key_list)
print('value_list ->', value_list)
#if you have list of keys and values you can map them into a dictionary
#using zip() object - to create new dictionary
mapping = zip(key_list, value_list)
print('mapping ->', mapping)
dict_new = dict(mapping)
print('dict_new ->', dict_new)
print("'k3' in dict_new ->", 'k3' in dict_new)
print("'k3' not in dict_new ->", 'k3' not in dict_new)
