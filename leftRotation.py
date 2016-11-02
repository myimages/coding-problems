def processFile(filename):
    with open(filename, 'r') as f:
        # Input:
        # numberOfIntegers numberofLeftRotations
        # Space Separated Integers
        n, d = f.readline().split(" ")
        n = int(n)
        d = int(d)
        # Convert the space separated string of numbers
        # into a list of integers
        # Note: It assumes this is on a single line. Might be a poor assumption.
        arr = f.readline().split(" ")
        i = 0
        for num in arr:
            arr[i] = int(num)
            i += 1
        return d, arr


def leftRotation (arr, d):
    # Perform d left rotations on array
    newArr = [None] * len(arr)
    i = 0
    while d > len(arr):
        d -= len(arr)
    while i < len(arr):
        # This works because -i indexing means something in Python
        # Would not work in most languages.......
        newArr[i - d] = arr [i]
        i += 1
    print(arr)
    print(newArr)

d, arr = processFile("leftRotation.txt")
newArr = leftRotation(arr, d)
