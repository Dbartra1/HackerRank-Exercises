def imp():
    with open('sample.txt', 'r') as f:
        numList = [int(line.strip().split(',')) for line in f]

def main(numList):
    imp()
    newNum = []
    for x in numList:
        for y in numList:
            if x + y == 2020:
                print (x, y)
                newNum = x * y
                print (newNum)