import os, json, time

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
phonebook[time.time()] = {
    "name": name,
    "address": address,
    "email": email,
    "phone": phone
}

# save data_file
with open(data_file, "w") as f:
    json.dump(phonebook, f)