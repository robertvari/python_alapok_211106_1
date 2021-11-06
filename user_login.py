username = "robert"
password = "testpas123"

user_response = input("Username?")

while user_response != username:
    print("Username doesn't exist...")
    user_response = input("Username?")


user_response = input("Password?")
while user_response != password:
    print("Wrong password...")
    user_response = input("Password?")

print("Welcome in the club!")