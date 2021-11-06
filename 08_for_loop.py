names = ["robert", "csaba", "kriszta", "tamás", "csilla"]

# sima for loop
#for name in names:
    #print(name)

# skip item in a list
for name in names:
    if name == "kriszta":
        continue
    print(name)


for name in names:
    if name == "kriszta":
        break
    print(name)

for name in names:
    if names.index(name) == 3:
        break


for index, name in enumerate(names):
    print(index, name)