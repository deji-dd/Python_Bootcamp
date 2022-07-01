def say_hello():
    print('hello')


say_hello()
def say_hello(name='Default'):
    print(f'Hello {name}')


say_hello('deji')
def add_num(num1, num2):
    print(num1 + num2)
    return num1 + num2


result = add_num(10, 20)
