try:
    result = 10 + 10
except TypeError:
    print("Hey it looks like you aren't adding correctly!")
else:
    print(f"Add went well!\n{result}")


try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except ValueError:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes, thank you!")
            break
        finally:
            print("End of function.")


ask_for_int()
