#!/bin/python3

import math
import os
import random
import re
import sys


def main():
    n = int(input("Enter a number: "))
    while True:
        if (n % 2) != 0:
            print ("Weird")
            break
        if (n % 2) == 0:
            if n in range (2,5):
                print ("Not Weird")
                break
            elif n in range (6,21):
                print ("Weird")
                break
            elif n > 20:
                print ("Not Weird")
                break
            else:
                pass


if __name__ == '__main__':
    #n = int(input().strip())
    main()
