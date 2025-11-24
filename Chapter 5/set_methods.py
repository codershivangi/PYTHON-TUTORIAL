s = {1,5,32,54,5,5,5,"Harry"}

s.remove(1)
print(s, type(s))
#print(s, type(s))

# Methods 

# 1. add()

#s.add(566)
#print(s, type(s))

# 2. clear()
#s.clear()
#print(s)

# 3. copy()
new_set = s.copy()
print(new_set)

# 4. difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))