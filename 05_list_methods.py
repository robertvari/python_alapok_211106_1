names = ["Robert", "Kriszta", "Csaba", "Tamás"]

print(names)

# insert items into list
names.append("John")
print(names)

names.insert(1, "Csilla")
print(names)

# delete/remove element from list
names.remove("Csaba")
print(names)

del names[0]
print(names)

# replace element in list
names[-1] = "Balázs"
print(names)

names.append("Csilla")
names.remove("Csilla")
del names[-1]
print(names)

# clear list
names.clear()
print(names)