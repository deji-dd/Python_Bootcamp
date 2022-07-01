"""
A very simple script to use pylint on
"""
def myfunc():
    """
    A simple function
    :return: first and second
    """
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()


def cap_text(text):
    """
    Input a string
    :param text:
    :return: Capitalized string
    """
    return text.title()
