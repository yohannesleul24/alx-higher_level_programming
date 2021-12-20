#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Exact same object. True if the object is exactly an instance
    of the specified class, otherwise False
    Args:
        obj:
        a_class:
    Return: True or False"""
    return(type(obj) == a_class)
