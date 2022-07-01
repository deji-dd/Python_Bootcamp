def hello():
    return 'Hi Deji!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

def new_decorator(original_func):
    def wrap_func():
        print('some extra code, before the original function')
        original_func()
        print('some extra code after the original function')
    return wrap_func()


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')
