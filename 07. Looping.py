# In python, you can loop through elements like this

# Using the range function that builds a set of value in the given range
for number in range(10):
    print(number)

print('=========================')
# You can also add breaking conditions to your loop
# the 'continue' means to skip
for number in range(10):
    if number is 1:
        continue
    elif number > 5:
        break
    print(number)


print('=========================')
# You can also loop using while
number = 0
while number < 10:
    print(number)
    number += 1
