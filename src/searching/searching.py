def linear_search(arr, target):
    index = 0
    for elem in arr:
        if elem is target:
            return index
        index += 1
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # TODO:
    # find the length of the array
    # divide that in half and see if the mid is what we are looking for
    # if the mid is the target, then return it
    # if the mid is lower than our target, take the left side and divide that in half and compare
    # if the mid is higher than our target, that the left side and divide that in half and compare
    # repeat steps each time you divide in half 
    # length = len(arr) -1
    if len(arr) <= 0:
        return -1
    mid = (len(arr) -1) // 2 
    low = 0 
    high = len(arr) -1
    # index = 0

    while low != high:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
        # go left and eliminate the mid and everything else on the right
            low = mid +1
        elif arr[mid] > target:
        # go right and eliminate the mid and everything else on the left
            high = mid -1
        mid = (high + low) // 2

    if arr[mid] == target:
        return mid
        # index += 1
    return -1 # not found
        

# print(binary_search([1,2,3,4,5,6], 3))
