#!/usr/bin/python3
def magic_string(n=0):
    magic_string.n = getattr(magic_string, "n", 0) + 1
    return ("Bestschool, " * (magic_string.n - 1) + "Bestschool")