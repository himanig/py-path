#FirstName = input('Please Enter your First Name: ')
#LastName = input('Please Enter your Last Name: ')
#print(FirstName + LastName)
#print('string reversed')
#str_list1 = list(FirstName)
#str_list2 = list(LastName)
#str_list1.reverse()
#str_list2.reverse()
#print(FirstName + LastName)
#print(str(str_list1) + str(str_list2))

#1
name = input('First and Last name : ')

words = name.split(" ")

for word in words:
    lastindex = len(word) - 1
    for index in range(lastindex, -1, -1):
        print(word[index], end='')
    print(end=' ')
print(end='\n')

#2

name = input('First and last name : ')

first, last = name.split()

print(first[::-1], last[::-1])
