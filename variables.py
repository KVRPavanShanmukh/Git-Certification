#playing with variables
# Defining variables

x =5
y =6
z=x*y
print(z)

# Defining a string variable
x="Pavan Shanmukh Kakarla"
x=6;
#the last declaration of x will be the value of x
# Printing the value of x
print(x)

#typecasting
x=str(3)
y=int(3)
z=float(3)

print(x)
print(y)
print(z)
# Printing the types of the variables
print(type(x))
print(type(y))

#Strings
x="Pavan Shanmukh Kakarla"
print(x)
#both are the same
x='Pavan Shanmukh Kakarla'
# Printing the value of x
print(x)
#but the variables are case sensitive
X="Pavan Shanmukh Kakarla"
# Printing the value of X
print(X)
# Printing the type of x
print(type(x))
# Printing the type of X
print(type(X))

#IDENTIFIERS ARE SAME AS JAVASCRIPT,C,C++
# Variable names can contain letters, numbers, and underscores
# Variable names cannot start with a number
# Variable names are case-sensitive
# Variable names cannot be a reserved keyword in Python
# Examples of valid variable names

#Assigning multiple varialbes in one line
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
#Assigning multiple variables to same value
d = e = f = 4
print(d)
print(e)
print(f)

#Strings get concatinated when the + operator is used
a="Hello"
b="World"
# Concatenating strings
c = a + " " + b
# Printing the concatenated string
print(c)

#Global Variables
# Global variables are defined outside of any function
x="SPS"
def func():
    print("Python is taught by", x)

func()#calling the function

# Global variables can be modified inside a function using the global keyword
x="SPS"
def myFunc():
    x = "Pavan Shanmukh Kakarla"  # Modify the global variable
    print("Python is taught by", x)

myFunc()  # Calling the function

print("Python is taught by", x)  # Printing the global variable
# Global variables can be modified inside a function using the global keyword

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "SPShanmukh"

myfunc()

print("Python is " + x)
#but the variable declared out of the function can be
#overridden by the variable declared inside the function
#when the function is called
