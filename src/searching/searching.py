def linear_search(arr, target):
    # Your code here
    # for every element in the array,
    # compare your target to that element and see if it matches
    for i in range(len(arr)): 
  
        if arr[i] == target: 
            return i 

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    mid = 0 
    # we are searching in between the start and the end indecies
    start = 0 
    end = len(arr) - 1
    # this is just to keep track of the search during each step
    step = 0

    while start <= end:
        print("Subarray in step {}: {}".format(step, str(arr[start:end+1])))
        step = step + 1
        mid = (start + end) // 2

        if target < arr[mid]:
            # eliminate the right side 
            end = mid - 1
        elif target > arr[mid]: 
            # eliminate the left side 
            start = mid + 1 
        else:
            return mid

    return -1  # not found/empty arr
