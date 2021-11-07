import os

if os.path.exists("user_data.txt"):
    print("user_data exists")

    with open("user_data.txt") as f:
        print(f.read())
else:
    user_name = input("Your name?")
    user_email = input("Your email?")

    with open("user_data.txt", "w") as f:
        f.write(f"{user_name}\n{user_email}")