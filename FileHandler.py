"""
I will choose this approach because I have a case
What if the file is deleted before the statement to open and read the file?

The former approach is prone to this condition
Hence I will choose try except to manage that Exception case
"""


def get_contents(fname):
    """
    The function get_contents takes a single parameter fname, which is the name of the file to be read.
    It attempts to open and read the file using open() and read()
    If successful, it returns the contents of the file.
    If a FileNotFoundError is raised (meaning the file does not exist), the function catches the exception and returns None.
    :param fname: 'path/to/the/file'
    :return: it will return either str or None
    """
    try:
        f = open(fname).read()
        return f
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    print(get_contents("README.md"))

