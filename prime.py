#FOR Loop
for outer in range(2,10):
    for inner in range(2,outer):
        if not outer % inner:
            print(outer, '=', inner, '*', int(outer / inner))
            break
    else:
            print(outer, 'is prime')

#dictionary
greek = {'a': 1, 'b': 2, 'c': 3}
for key in greek:
    if key == 'b':
        continue
    print(key, greek[key])
