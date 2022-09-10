"""
Filesystem related utilities
"""

import pathlib

class FileFilters:
    """
    Filters for filenames and stuff
    """
    @staticmethod
    def remove_ext(string):
        """
        Removes the file extension from the specified string
        """
        return pathlib.Path(string).stem
        
class DirectoryFilters:
    """
    Filters out unwanted files from a List of directories
    """
    @staticmethod
    def filter_python_autogen(lst):
        """
        Remove all python-generated files from the list
        """

        new_lst = lst
        new_lst.remove("__init__.py")
        new_lst.remove("__pycache__")

        return new_lst
