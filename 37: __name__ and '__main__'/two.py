# understanding the __name__ = '__main__' call
import one

print('\n')
print("Top level in two.py")
print('\n')
one.func()
print('\n')


if __name__ == '__main__':
    print("two.py is being run directly")
else:
    print("two.py has been imported")
