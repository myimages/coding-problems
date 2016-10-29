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
        arr = f.readline().split(" ")
        i = 0
        for num in arr:
            arr[i] = int(num)
            i += 1
        return d, arr


def leftRotation (arr, d):
    # Perform d left rotations on array
    print("")

d, arr = processFile("leftRotation.txt")
print(d)
print(arr)
