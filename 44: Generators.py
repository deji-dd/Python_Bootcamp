def create_cubes(n):
    for x in range(n):
        yield x ** 3

def gen_fibon(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def simple_gen():
    for x in range(3):
        yield x


g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
