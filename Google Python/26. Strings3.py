# Video 45
# String methods
# Converting to upper and lower cases
print("Mountains".upper())
print("Mountains".lower())

answer = "yes"
if answer.upper() == "YES":
    print("User said yes")
else:
    print("User said no")
# Remove whitespaces using strip()
#lstrip(), rstrip()
print("  yes  ".strip())
# Count occurence of a character
print("The number pf times e occurs in this string is ".count("e"))
# Return last substring
print("Forest".endswith("rest"))
# Check if its numeric
print("Forest".isnumeric())
print("1234".isnumeric())
# Joining together strings
print(" ".join(["This","is","a","phrase","joined","by","spaces"]))
print("...".join(["This","is","a","phrase","joined","by","triple","dots"]))
# Splitting a string to substrings
print("This is another example".split())