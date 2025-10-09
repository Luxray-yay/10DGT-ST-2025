# Creating an input system for our coffee program
# Elisabeta Bayer
# Date: 10/10/2025

# Version 1
# TODO: ask the user if they like coffee
#       Record the answer
#       Give a response back to the user

# Ask the user whether they lke coffee or not
like_coffee = input("Do you like coffee? ")
print(f'Your answer was "{like_coffee}".')

if like_coffee == "yes" or "Yes" or "y" or "yep":
    print("That is great! I like coffee too.")

else:
    print("You are missing out! Why not give it a try?")



