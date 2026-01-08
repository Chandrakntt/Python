# Lists (mutable, ordered)

fruits = ["apple","banana","cherry"]
fruits.append("orange")                 # Add item
fruits[0] = "apricot"                   # Modify
last = fruits.pop()                     # Remove last


# Tuples (immutable, ordered)

coordinates = (10,30)
# coordinates[0] = 15                   # ERROR! Cannot modify


# Dictionaries (Key-value pairs)

person = {"name":"John","age":30}
person["city"] = "New York"             # Add key-value
age = person.get("age")                 # Get value


# Sets (unique, unordered)

unique_numbers = {1, 2, 3, 4, 4, 3}     # {1, 2, 3, 4}

