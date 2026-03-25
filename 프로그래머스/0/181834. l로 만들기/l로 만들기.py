def solution(myString):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k']
    myList = []
    for i in range(len(myString)):
        if myString[i] in alphabet:
            myList.append('l')
        else:
            myList.append(myString[i])
    return ''.join(myList)