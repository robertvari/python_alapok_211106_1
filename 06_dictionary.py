#       root key       value
phonebook = {
    "0620123456": {"name": "Róbert", "address": "Debtrecen", "email": "robert@gmail.com"},
    "0630857463": {"name": "Kriszta", "address": "Eger", "email": "kriszta@gmail.com"},
    "0620647392": {"name": "Tamás", "address": "Budapest", "email": "tamas@gmail.com"}
}

print(
    phonebook["0620647392"]["name"],
    phonebook["0620647392"]["address"],
    phonebook["0620647392"]["email"]
)

# unique root key
phonebook["0620555 66 77"] = {"name": "Csilla", "address": "Pécs", "email": "csilla@gmail.com"}

# override element in dictionary
phonebook["0620123456"] = 10

# remove from dictionary
del phonebook["0620555 66 77"]
print(phonebook)

