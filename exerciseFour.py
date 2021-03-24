with open("romeo.txt") as f:
    theList = sorted(word.strip(" ") for line in f for word in line.split())

theNewList = sorted(theList, key=str.lower)
print(theNewList)
