import math
def binary_search(arr, target):
    arr.sort()
   
    left = 0
    right = len(arr) - 1

    while left <= right:   
        mid = math.floor((left + right) / 2)

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            return arr.index(target)
    
    return -1        

print(binary_search([1,4,111,34,5,56,87,58,12,-4], 5))

def mat(mat):
    lst=[]
    for arr in mat:
        sum=0
        for element in arr:
            sum+=element
        lst.append(sum)             
    print(lst)
                
mat([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ])

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7))