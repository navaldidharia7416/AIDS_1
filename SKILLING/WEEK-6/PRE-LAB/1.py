def printTwoElements(arr, size):
    for i in range(size):
        if arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            print("The repeating element is ", abs(arr[i]))
arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
printTwoElements(arr, n)

