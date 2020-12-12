#!/usr/bin/env python3
"""
The provided code stub reads and integer, n , from STDIN. 
For all non-negative integers i < n, print i^2 . 
"""

def main():
    n = int(input("N: "))
    for i in range (0, n):
        print (i*i)
    


if __name__ == '__main__':
    #n = int(input())
    main()



