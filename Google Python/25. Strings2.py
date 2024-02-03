# Video 44
message="A kong string with a silly typo"
new_message=message[0:2]+"l"+message[3:]
print(message)
print(new_message)
message="This is a new message"
print(message)
message="Add another one"
print(message)
# Obtaining index of a character in a string
pets ="Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))
# Check for a substring in string
print("Dragon" in pets)
print("Cats" in pets)