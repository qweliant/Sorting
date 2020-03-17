# TO-DO: Complete the selection_sort() function below 
# 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # for every element in the array, look for a         
        # for index in range(i, len(arr)):
            if arr[index] < arr[smallest_index]:
                smallest_index = index

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 0
    while i < len(arr)-1:
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
                i = 0
        i += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    return arr