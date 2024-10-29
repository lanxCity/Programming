# ==> Tuple
'''
t_1 = (2, 1, 3, 4)
t_2 = tuple([chr(65 + i) for i in range(26)][:])
t_3 = (2)  # This (with a value without comma)is considered as int
t_4 = (2,)  # This is considered as tuple

print(t_1)
print(t_2)
print(type(t_2))
print(t_3)
print(type(t_3))
print(t_4)
print(type(t_4))

t_5 = t_1 + t_2   # It supports concatenation as list
print(t_5)
l_1 = list(t_1) + list(t_2)  # Converts tuple to list
print(l_1)

t_6 = (10,)*5
l_2 = [10]*5

print(t_6)
print(l_2)

print('\n=========================> Set')
# ==> Set  (No indexing)
# -> We can add to set using a set method, 'add'
set1 = {2, 1, 3, 4, -10, 'a', "Lanx", 0, -5.789, -5}  # The items are unordered
set2 = set([chr(65 + i) for i in range(26)][:])
set3 = {'a'}
# Duplicated items would be removed e.g True and False ~= 0 & 1
set4 = {2, 1, 3, 'a', "Lanx", 0, -5.789, False, -5, True}
# Empty set is not created like this, else, empty dictionary would be created
set5 = {}
# For empty set, we'll use set object
set6 = set()

for i in set1:  # It works
    print(i)

print(set1)
print(set2)
print(set3)
print(set4)
print(type(set5))
print(type(set6))


set7 = {'a'}
set7.add('b')
print(set7)
set7.update(['c', 'd', 'e'])  # It spreads the element into the set
print(set7)
set7.update({'c', 'j', 'e'})
print(set7)
set7.update('c', 'f', 'e')
print(set7)
# NB: Only immutable items can be added as element of a set
set7.add(('c', 'f', 'e'))  # it works
print(set7)
set7.add(['c', 'f', 'e'])  # Error
print(set7)

# -> Set operations
set1 = set([i for i in range(5)])
set2 = set([i for i in range(10, 5, -1)])
set3 = set([i for i in range(10, 15)])

print(set1.union(set2))
print(set1 | set2)
print(set1.union(set2, set3))
print(set1 | set2 | set3)



# -> Dictionary

dic1 = {}
dic2 = {'name': 'Lanx', 'age': 46}
dic3 = dict({'name': 'Lanx', 'age': 46})
dic4 = dict([('name', 'Lanx'), ('age', 46), ('gender', 'M')])

print(dic1)
print(dic2)
print(dic3)
print(dic4)

del dic4['age']
dic4.pop('name')  # To delete the last item
print(dic4)

dic4['age'] = 35
print(dic4)
print({}.fromkeys(['age', 'name', 'level'], 67))
# {}.popitem()  # To delete the last item

'''






data = {}
data.update({'name': 'Lanx'})

print(list(data.items()))


