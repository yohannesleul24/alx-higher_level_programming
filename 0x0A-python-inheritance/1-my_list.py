#!/usr/bin/python3
"""
inherits from list
"""

class MyList(list):
    """
    class of Mylist inherite from list
    """

    def print_sorted(self):
        """
        print a list
        :return:
        """
        print(sorted(self))
