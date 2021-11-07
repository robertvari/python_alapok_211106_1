my_set = {1, 2, 3}

# add single element
my_set.add(4)

# add multiple elements
my_set.update([5, 6, 7])

# you can delete not existing elements
#my_set.discard(20)

# can only delete existing element
#my_set.remove(30)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# merge two sets
print(A | B)

# intersection
print(A & B)

# Difference
print(A - B)

# Symmetrical difference
print(A ^ B)