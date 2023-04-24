# List
fruits_list = ["apple", "banana", "cherry"]
fruits_list.append("orange")
print(fruits_list)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Dictionary
fruits_dict = {"apple": 1, "banana": 2, "cherry": 3}
fruits_dict["orange"] = 4
print(fruits_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'orange': 4}

# Tuple
fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple.append("orange")  # Throws an AttributeError since tuples are immutable
print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry')

# Set
fruits_set = {"apple", "banana", "cherry"}
fruits_set.add("orange")
print(fruits_set)  # Output: {'cherry', 'orange', 'banana', 'apple'}
