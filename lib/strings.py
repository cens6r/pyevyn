"""
Strings: provides useful string utilities
"""

class Strings:
    """
    Contains the functions you installed this library for :^)
    """

    @staticmethod
    def lines(char, length):
        """
        Prints out a line with the specified character and length
        """

        for _ in range(length):
            print(char, end="")
        print("")

    @staticmethod
    def pad_spaces(string, size):
        """
        Pads the string with spaces
        """
        return (" " * size) + string + (" " * size)
