import random

min_number = 1
max_number = 10
max_tries = 3

magic_number = random.randint(min_number, max_number)

print("="*50, "MAGIC NUMBER GAME", "="*50)
print(f"I'm thinking of a number between {min_number} and {max_number}.\nCan you guess my number?")
print("="*120)

user_response = int( input("Your guess:") )

while user_response != magic_number:
    max_tries -= 1

    if max_tries == 0:
        print("You have no more tries :(((")
        break

    print(f"Wrong answer. You have {max_tries} tries left.")
    user_response = int( input("Your guess:") )

if user_response == magic_number:
    print(f"You win! My number was: {magic_number}")
else:
    print("Game over... maybe next time!")