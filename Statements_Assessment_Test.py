# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print([i for i in 'Print only the words that start with s in this sentence'.split() if i[0].lower() == 's'])

# use of range() and get even numbers in between 0 to 10
print([i for i in range(1, 11) if i % 2 == 0])

# Use of list comprehension to find numbers between 1 - 50 which is divisible by 3.
print([i for i in range(1, 50) if i % 3 == 0])

# Go through the string below and if the length of a word is even print "even!"
statemen = 'Print every word in this sentence that has an even number of letters'
[print(f'{i}: Even!') for i in statemen.split() if len(i) % 2 == 0]

# "Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"".

for i in range(1, 100):
    if i % 3 == 0:
        print(f"{i}:Fizz")
    elif i % 5 == 0:
        print(f"{i}:Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i}:FizzBuzz")

# Use List Comprehension to create a
# list of the first letters of every word in the string below:
print([i[0].upper() for i in 'Create a list of the first letters of every word in this string'.split() ])