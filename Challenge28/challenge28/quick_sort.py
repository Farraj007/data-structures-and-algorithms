from array import array


def QuickSort(arr, left, right):
    """
    QuickSort function
    """
    if len(arr) == 0:
        raise Exception("Array is empty")
    
    if left < right:
        position = Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)
    
def Partition(arr, left, right):
    """
    Partition function
    """
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    """
    Swap function
    """
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp

if __name__ == "__main__":
    # arr=[2,3,5,7,13,11]
    arr = [20,18,12,8,5,-2]
    # arr=[5,12,7,5,5,7]
    QuickSort(arr,0,len(arr)-1)
    print(arr)