fruits = ["apple", "banana", "cherry", "date"]
# Unpacking the list into variables
a, b, c, d = fruits
# Printing the unpacked variables
print(a)   # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry
print(d)    # Output: date

# Unpacking with an asterisk to capture remaining items
first_fruit, *remaining_fruits = fruits
# Printing the first fruit and remaining fruits
print(first_fruit)         # Output: apple
print(remaining_fruits)    # Output: ['banana', 'cherry', 'date']
# Unpacking with an asterisk at the end
*initial_fruits, last_fruit = fruits
# Printing the initial fruits and the last fruit
print(initial_fruits)  # Output: ['apple', 'banana', 'cherry']
print(last_fruit)      # Output: date

# Unpacking a tuple
coordinates = (10, 20, 30)
x, y, z = coordinates
# Printing the unpacked coordinates
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

# Unpacking a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
name, age, city = person.values()
# Printing the unpacked values
print(name)  # Output: Alice
print(age)   # Output: 30
print(city)  # Output: New York
# Unpacking with a function return value
def get_user_info():
    return "Bob", 25, "Los Angeles"
name, age, city = get_user_info()
# Printing the unpacked user info
print(name)  # Output: Bob
print(age)   # Output: 25
print(city)  # Output: Los Angeles
# Unpacking with a function that returns a list
def get_numbers():
    return [1, 2, 3, 4, 5]
a, b, *rest = get_numbers()
# Printing the unpacked numbers
print(a)      # Output: 1
print(b)      # Output: 2
print(rest)   # Output: [3, 4, 5]
# Unpacking with a function that returns a tuple
def get_coordinates():
    return (100, 200, 300)
x, y, z = get_coordinates()
# Printing the unpacked coordinates

