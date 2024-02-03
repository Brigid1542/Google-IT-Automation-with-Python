# Video 29
# Modifying contents of a list
fruits =["Pineapple","Banana","Apple","Melon"]
print("Original list: ")
print(fruits)
fruits.append("Kiwi")
print("After appending: ")
print(fruits)
# Inserting element to specific index
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(30,"Peach")
print(fruits) 
# Removing elements using remove > String
fruits.remove("Melon")
print(fruits)
# Removing elements using pop > index > Integer
fruits.pop(3)
print(fruits)
# Reassigning
fruits[2]="Strawberry"
print(fruits)