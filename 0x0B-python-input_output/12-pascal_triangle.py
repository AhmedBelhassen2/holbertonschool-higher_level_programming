#!/usr/bin/python3
"""  pascal Triangle """


def pascal_triangle(n):
    """ print pascal triangle """
    if n <= 0:
      return []  

    t = [[l]]

    for i in range