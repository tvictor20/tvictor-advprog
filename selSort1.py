def smallValue(oList):
    min = oList[0]
    for i in oList:
        if i < min:
            min = i

    oList.remove(min)
    return oList, min


def main():
    oList = [4,7,11,8,1,54,2,2] #original list
    fList = [] #final list
    print oList
    for i in range(len(oList)):
        oList, x = smallValue(oList)
        fList.append(x)

    print fList

main()
