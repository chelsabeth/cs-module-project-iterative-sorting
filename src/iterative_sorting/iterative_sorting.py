# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TODO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for elem in range(i + 1, len(arr)):
            if arr[elem] < arr[cur_index]:
                cur_index = elem

        # TODO: swap
        # Your code here
        # after finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
        # We go through the list as many times as there are elements
    for i in range(len(arr)):
        # We want the last pair of adjacent elements
        for elem in range(len(arr) - 1):
            if arr[elem] > arr[elem+1]:
                # Swap
                arr[elem], arr[elem+1] = arr[elem+1], arr[elem]



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
