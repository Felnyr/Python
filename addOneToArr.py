# Add 1 to the given array and prints sum of all elements

arr = [1,3,4,5,9]

def addOne(arr):

    newArr = str(arr)

    for x in newArr:
        if x == "[" or x =="]" or x == "," or x ==" ":
            newArr = newArr.replace(x, "")

    return list(str(int(newArr) + 1))
    
print(addOne(arr))
