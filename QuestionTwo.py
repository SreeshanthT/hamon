"""
def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 0
    return r

the given code seems like to get the count of each string character, but there is an issue that the
base case the dict assign the value zero will get the wrong output
"""


def f(s):
    """
    Count the occurrences of each character in a string.

    Parameters:
        s (str): The input string.

    Returns:
        dict: keys as character and value will be the occurrences

    Example:
    >>>f('hamon')
    {'h': 1, 'a': 1, 'm': 1, 'o': 1, 'n':1}
    """
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    return r


def f_v1(s):
    """
    Here is a different approach to reduce the line of code but the same result
    using comprehension, count, and set

    But also count the occurrences of each character in a string.

    Parameters:
        s (str): The input string.

    Returns:
        dict: keys as character and value will be the occurrences
    """
    return {i: s.count(i) for i in set(s)}


if __name__ == "__main__":
    print(f_v1("hamon"))
    print(f("hamon"))
