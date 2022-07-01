# LEGB Rule:
# L: Local -> Names assigned in any way within a function (def or lambda), and not declared global in that function.
# E: Enclosing function locals -> Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# G: Global (module) -> Names assigned at the top-level of a module file, or declared global in a def within that file.
# B: Built-in (Python Bootcamp) -> Names preassigned in the built-in names module: open, range, SyntaxError...
x = lambda num: num ** 2  # Example of Local function
name = 'this is a global string'  # Global name function


def greet():
    name = 'sammy'  # Enclosing name Function
    # if the variable name is commented out then the function uses the global name variable from the outer scope

    def hello():
        name = "I'm local"  # Local name function
        # if the local variable name is commented out, then the function uses the enclosing name variable from the
        # outer scope. and if that is commented out, then the function uses the global name variable.
        print('hello ' + name)

    hello()


greet()
x = 50
def func():
    global x
    print(f'X is {x}')
    x = 'new value'  # local reassignment on a global variable
    print(f'i just locally changed x to {x}')


print(x)
func()
print(x)
