# Functions within a Python program are a collection or block of code that is executed only when you call for them, and they return data as a result.
# This segment of the Python course will teach you about creating and calling functions, along with different arguments, global and local variables, and recursion.
# Subjects covered in functions in Python:
# What are Functions
# Modularity and code reusability
# Creating functions
# Calling functions
# Passing Arguments
# Positional Arguments
# Keyword Arguments
# Variable-length arguments (*args)
# Variable Keyword length arguments (**kargs)
# Return keyword in Python
# Passing function as an argument
# Passing function in return
# Global and local variables
# Recursion



# passing function as an argument


def greet(name):
    return f"Hello, {name}!"

def execute_function(func, value):
    return func(value)

result = execute_function(greet, "Alice")
print(result)  # Output: Hello, Alice!


# Passing Function in Return
# You can also return functions from other functions. This is known as higher-order functions and is useful for closures.
#
# Example:
#
# python
# Copy
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)  # Returns a function that multiplies by 2
print(double(5))  # Output: 10

#  Global and Local Variables
# Variables in Python can either be global or local.
#
# Local variables are defined within a function and are only accessible inside that function.
# Global variables are defined outside of any function and can be accessed anywhere in the program.
#
# If you need to modify a global variable inside a function, you can use the global keyword.
#
# python
# Copy
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # Output:

# Summary of Key Concepts:
#
# Functions in Python allow you to group code and reuse it.
# Modularity makes your code easier to maintain, and code reusability reduces redundancy.
# Functions can accept positional, keyword, and variable-length arguments (*args and **kwargs).
# Functions can return values using the return keyword.
# Functions can be passed as arguments or returned from other functions.
# Global and local variables have different scopes in Python.
# Recursion is used for problems that can be broken into smaller, similar subproblems.
l1 = list()
# l2 = [1, 2, 3 ,4]
# l3 = []
# sample_list = [10, 20, 30, 40,50]
# print(sample_list)
#
sample_list1 = [1, 2, 3, 4, 5, 6, 'messege', "number"]
# print(sample_list1)
# print(type(sample_list1))
# sample_list1.append("charachter")
# print(sample_list1)
# user_list = [ "age", "height", "gender"]
#
types_of_denomination = [1, 2, 5, 10, 20, 50, 100, 200, 500]
# print("type of denomination",types_of_denomination)


