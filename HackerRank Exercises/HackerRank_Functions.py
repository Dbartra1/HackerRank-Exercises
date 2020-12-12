#!/usr/bin/env python3
"""
Given a year, determine whether it is a leap year. 
If it is a leap year, return the Boolean True, otherwise return False.
"""

def is_leap():
    year = int(input("enter a year: "))
    leap = False
    if (year % 4) == 0:
        leap = True
        if (year % 100) == 0:
            leap = False
            if (year % 400) == 0:
                leap = True
    print (leap)
    return leap

is_leap()
