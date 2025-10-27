# Enclosing
# This scope exists for nested functions.
# If a function is defined inside another function, 
# the inner function can access names from its enclosing (outer) function's scope.
# Variables in the enclosing scope are accessible to both the inner and outer functions.

def outer_function():
    enclosing_var = "I am from the enclosing scope"

    def inner_function():
        print(enclosing_var) # inner_function can access enclosing_var

    inner_function()

outer_function()