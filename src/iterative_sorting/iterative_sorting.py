# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        sorted_boundary = i
        smallest_index = sorted_boundary
        # TODO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # iterate through the unsorted portion of the arr
        # finds the index of the smallest elem in the unsorted portion 
        for unsorted_index in range(sorted_boundary, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TODO: swap
        # Your code here
        # after finding the index of the smallest elem of the unsorted regions, swap with the first unsorted item
        arr[smallest_index], arr[sorted_boundary] = arr[sorted_boundary], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
        # traverses the arr
        # loop until no more swaps
    swaps_occurred = True

    while swaps_occurred:
        swaps_occurred = False
        for elem in range(0, len(arr) - 1):
            if arr[elem] > arr[elem+1]:
                # Swap
                arr[elem], arr[elem+1] = arr[elem+1], arr[elem]
                swaps_occurred = True

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
