my_map = {
    "name": "Edmond",
    "age": 27,
    "city": "Nakuru",
    "email": "edmondbonventure@gmail.com"
}

# Access
print(my_map["city"])

# Add value

my_map["country"] = "Kenya"
print(my_map)

# Delete Value
del my_map["email"]

print(my_map)


class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, value):  # Chaining
        h = hash(key) % self.size # Get Index
        for pair in self.table[h]:   # Search in the bucket or the whole index
            if pair[0] == key:
                pair[1] = value         # Update value if key exists
                return
        self.table[h].append([key, value])

    def get(self, key):
        h = hash(key) % self.size
        for pair in self.table[h]:
            if pair[0] == key:
                return pair[1]
            return None # Return None if key not found
        
hm = HashMap(10)
hm.put("name", "Edmond")
hm.put("age", 27)
hm.put("city", "Nakuru")
print(hm.get("city"))
print(hm.get("name"))
hm.put("name", "Edmond Bonventure")  # Update value
print(hm.get("name"))