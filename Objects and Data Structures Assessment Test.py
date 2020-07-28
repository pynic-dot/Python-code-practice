# Print out  'e' using indexing
s = 'Hello'
print(s[1])

# Reverse the string
print(s[::-1])

# Two method to produce letter 'o'
print(s[4])
print(s[-1])

# Lists Build list [0,0,0] in two different way
s = []
for i in range(3):
    s.append(0)
print(s)
print([0, 0, 0])
print([0]*3)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list_1 = [1, 2, [3, 4, 'Hello']]
list_1[2][2] = 'Hello Goodbye'
print(list_1)

# Sort the list
list_4 = [5, 3, 4, 6, 1]
print(sorted(list_4))

# Dictionary
dit = {'simple_key': 'Hello0'}
print(dit['simple_key'])

dit = {'k1': {'k2': 'hello1'}}
print(dit['k1']['k2'])
dit = {'k1': [{'nest_key': ['this is deep', ['Hello2']]}]}
print(dit['k1'][0]['nest_key'][1][0])
dit = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello3']]}]}]}
print(dit['k1'][2]['k2'][1]['tough'][2][0])

# There are two nested loop
list1 = [1, 2, [3, 4]]
list2 = [1, 2, {'k1': 4}]
print(list1[2][0] <= list2[2]['k1'])


