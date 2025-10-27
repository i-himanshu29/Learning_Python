# LEGB Rule in Action:

# When a name is referenced in Python, the interpreter searches for it in this 
# specific order: Local -> Enclosing -> Global -> Built-in. 
# If the name is found in any of these scopes, the search stops. 
# If the name is not found in any of these scopes, a NameError is raised.

# Local......
# This is the innermost scope.
# It includes names defined within the current function or a lambda expression.
# Variables declared inside a function are local to that function and 
# are only accessible from within its body.
# A new local scope is created each time a function is called.
local_var = "Himanshu"
def my_function():
    local_var = 10  # local_var is in the local scope of my_function
    print(local_var)
    # print(x)

my_function()
# print(local_var) # This would raise a NameError