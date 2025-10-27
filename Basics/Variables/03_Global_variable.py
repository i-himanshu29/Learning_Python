# This scope refers to names defined at the top level of a module or script.
# Variables declared outside of any function or class belong to the global scope.
# Global variables are accessible throughout the entire program, 
# including inside functions (though modification requires the global keyword).

global_var = "I am global"

def another_function():
    print(global_var) # another_function can access global_var

another_function()