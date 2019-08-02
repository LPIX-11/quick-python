# Dealing with lists in python since we use them a lot
x = [1, 2, 3, 4, 5, 6]

# Print list length
print(x, ' contains: ', len(x), ' items')

# len returns the number of items in contained an object

# ###

# If you need to slice list to extract values in a given range you can do
first = x[:3]
last = x[3:]

tLast = x[-2:]

print(first, ': first data extracted from the original list')
print(last, ': last data extracted from the original list')

print(tLast, ': last two elements extracted from the original list')

# ###

# Append a list to another list
x.extend([7, 8])
print(x, ': Appened [7, 8] list')

# If it's just appending a single object

x.append(9)
print(x, ': Appened 9\n')

# If it's about creating a list of lists

y = [14, 11, 13, 10, 12]

# This will be a list constituated of x and y lists
listLists = [x, y]

print(listLists, ': list of lists\n')

# ###

# If it's about sorting the lists

# the basic sorting
listLists[1].sort()

# the reverse sorting
listLists[0].sort(reverse=True)

# reversing the list of lists
listLists.sort(reverse=True)

print(listLists, ': sorted list of lists list')
print(listLists[0], ': sorted y list')
print(listLists[1], ': x list reversly sorted')


# ###

# Tuples
# In python, tuples are a lot like lists but they are immutable, once a tuple, it can't change it
# It's handy when performing functionnal programming or when interfacing with systems like Apache Spark

# Redeclaring x as a tuple
x = (1, 2, 3)

print(len(x))

# And you can do pretty much things that we've done earlier

# If you want to pass group of variables that you want to keep together you can use tuple
tupleVariables = (age, income) = "29,1200000".split(',')

(age, income) = "29,1200000".split(',')
print(tupleVariables, ': Tupled values')
print(age)
print(income)
