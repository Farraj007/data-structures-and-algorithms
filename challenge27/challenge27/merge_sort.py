

def Mergesort(arr):

    array_length = len(arr)
    if array_length > 1:
        mid = array_length // 2
        left = arr[0:mid]
        right = arr[mid:]
        Mergesort(left)
        Mergesort(right)
        merge(left, right, arr)
    return arr
        
def merge(left,right,arr):
    """
    merge function takes 3 arguments: left, right, array.
    left and right are the left and right halves of the array.
    arr is the array that is being sorted.
    """
    
    count1 = 0
    count2 = 0
    count3 = 0
    while count1 < len(left) and count2 < len(right):
        if left[count1] <= right[count2]:
            arr[count3] = left[count1]
            count1 += 1
        else:
            arr[count3] = right[count2]
            count2 += 1
        count3 += 1
    while count1 < len(left):
        arr[count3] = left[count1]
        count1 += 1
        count3 += 1
    while count2 < len(right):
        arr[count3] = right[count2]
        count2 += 1
        count3 += 1   
    
if __name__ == '__main__':
    print("jhjhjhexit")
    a=[0,10,-8,5,2,5]
    print(Mergesort(a))