# Create an empty list
my_list = []

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position
my_list.insert(1, 15)

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Remove the last element
my_list.pop()

# Sort the list
my_list.sort()

# Find and print the index of 30
print("The index of the value 30 in my_list is:", my_list.index(30))