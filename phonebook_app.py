import os, json

phonebook = {}
data_file = "phonebook.json"


# check data file
if os.path.exists(data_file):
    with open(data_file) as f:
        phonebook = json.load(f)

# get data from user
name = input("Your name?")
address = input("Your address?")
email = input("Your email?")

# add to phonebook dictionary
phonebook["name"] = name
phonebook["address"] = address
phonebook["email"] = email

# save data_file
with open(data_file, "w") as f:
    json.dump(phonebook, f)