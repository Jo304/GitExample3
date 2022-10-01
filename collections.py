fruits = ["apple", "banana", "strawberry", "orange", "peach"]

print(fruits[1])


fruits[4] = "nectarine"

print(fruits[4])

# A tple object, just like a list but "immutable"
fruits_tuple = ("apple", "banana", "strawberry", "orange", "peach")

# This line will throw an expection
#fruits_tuple[4] = "Nectarine"

fruit_locations = {
    "Bin 1": "apple",
    "Bin 2": "banana",
    "Bin 3": "strawberry",
    "Bin 4": "orange", 
    "Bin 5": "peach",
}

print(fruit_locations.get("Bin 3"))