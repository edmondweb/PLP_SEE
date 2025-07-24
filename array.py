# Index:   0  1   2    3   4
# Arrray: [5, 10, 15, 20, 25]

# arr[2]

# Define an array (List in python)

arr = [10, 20, 30, 40, 50]

# Accessing elements in an array

print(arr[2])

# Update the values

arr[3] = 60

print(arr)

print(arr[3])

# Insert at the end of the array

arr.append(70)

# Insert at a speecific position

arr.insert(3, 45)

# Delete an element

arr.pop(3)


print(arr)


# Search for a value

if 50 in arr:
    print("50 is present")
else:
    print("50 is not present")

