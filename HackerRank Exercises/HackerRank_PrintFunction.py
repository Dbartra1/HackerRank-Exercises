#!/usr/bin/env python3
'''
Without using any string methods, try to print the following:
123...n
'''
def main():
    n_list = list(range(1, n))
    n_list.append(n)
    new_list = ''.join(map(str, n_list))
    print (new_list)


if __name__ == '__main__':
    n = int(input())
    main()
