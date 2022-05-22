def insertion_sort(arr):
    if len(arr)==0 :
        raise Exception("Array is empty")
    for elements in range(1, len(arr)):
        if type(elements) != int :
            raise Exception("Array contains non-integer elements")
        element_position = elements - 1
        elemnet_sorting = arr[elements] 
         
        while element_position >= 0 and elemnet_sorting < arr[element_position]:
            arr[element_position+1] = arr[element_position]
            element_position -= 1

        arr[element_position + 1] = elemnet_sorting
    return arr


arr = [8,4,23,42,16,15]
print(insertion_sort(arr))