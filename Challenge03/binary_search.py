import math
def binary_search(arr, target):
    arr.sort()
   
    left = 0
    right = len(arr)

    while left <= right:   
        mid = math.floor((left + right) / 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return arr.index(target)
    return -1        

