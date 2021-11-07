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
phone = input("Phone?")
email = input("Email?")

# add to phonebook dictionary
phonebook[phone] = {
    "name": name,
    "address": address,
    "email": email
}

# save data_file
with open(data_file, "w") as f:
    json.dump(phonebook, f)