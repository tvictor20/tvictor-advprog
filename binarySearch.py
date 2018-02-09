#1/31/18

numList = range(100)
def binarySearch(numList, number):
    guess = round(len(numList)/2)
    if number > numList[guess]:
        for i in numList:
            if i < guess
