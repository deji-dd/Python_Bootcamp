import timeit

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str, range(n)))


stmt = """
func1(100)
"""
setup = """
def func1(n):
    return [str(num) for num in range(n)]
"""
print(timeit.timeit(stmt, setup, number=1000000))

stmt2 = """
func2(100)
"""
setup2 = """
def func2(n):
    return list(map(str, range(n)))
"""
print(timeit.timeit(stmt2, setup2, number=1000000))
