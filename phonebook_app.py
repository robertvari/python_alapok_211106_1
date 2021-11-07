import os, json

phonebook = {}
data_file = "phonebook.json"


# check data file
if os.path.exists(data_file):
    with open(data_file) as f:
        phonebook = json.load(f)
        print(phonebook)
# if not
    # get data from user
    # save data_file
