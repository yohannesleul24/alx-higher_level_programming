#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Exact same object. True if the object is exactly an instance
    of the specified class, otherwise False
    Args:
        obj:
        a_class:
    Return: True or False"""
    return(isinstance(obj, a_class))
