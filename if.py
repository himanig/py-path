#IF
age = 0
if age:
    print('false condition')
    print('wont execute')

age = 1
if age:
    print('True cond will be executed')

age = 17
if age >= 18:
    print('old enough to vote')
else:
    print('not old enough to vote')

score = 91
print('Grade: ', end=' ')
if score < 60:
    print('f')
elif 60 <= score < 70:
    print('d')
elif 70 <= score <90:
    print('b')
elif 90<= score <= 100:
    print('a')
else:
    print('default')

debug = True
if debug: print('Score:', score)

if score > 59:
    result = 'pass'
else:
    result = 'fail'
if debug: print('result: ', result)

score = 40
if debug: print('score: ', score)
result = 'pass' if score > 59 else 'fail'
if debug: print('result :', result)
