def linear_search(arr, target):
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    mid = 0 
    start = 0 
    end = len(arr) - 1
    step = 0

    while (start <= end):
        print("Subarray in step {}: {}".format(step, str(arr[start:end+1])))
        step = step + 1
        mid = (start + end) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]: 
            start = mid + 1 
        else:
            return mid

    return -1  # not found/empty arr
