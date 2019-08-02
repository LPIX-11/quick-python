# Dealing with dictionnaries
# In other laguages it's known as map | hash table | associative array
captains = {}
captains['Entreprise'] = 'Kirk'
captains['Enterprise D'] = 'Picard'
captains['Deep Space Nine'] = 'Sisko'
captains['Voyager'] = 'Janeway'

print(captains, ': full dictionnary')

# NB:
# 1. You can't retrieve a value using numeric key if it does not exist eg: captains[0]
# 2. If you try to retrieve a value with a key that doesn't exist, it will throw an exception
# In that case, it is recommended to use the dictionnary's get method, it will just return a None value
print(captains.get('Entreprise'), ': single element from the dictionnary\n')


# Looping through the  dictionnary
for ship in captains:
    print(ship)


# If it's about cleaning the dictionnary
captains.clear()
print(captains, ': after cleaning')
