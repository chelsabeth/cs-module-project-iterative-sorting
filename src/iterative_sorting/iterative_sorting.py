# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # NOTE:
    # saves min and index
    # sorted part and unsorted part
    # no switching until the end of the iteration
    # no item is "pulled out" of the array when comparing 
    # TODO:
    # takes the item/next item in the unsorted part and assigns that to be the lowest
    # goes thorugh the whole array and compares that value to each item
    # if another item in the arr is less than the current lowest, assign that to be the new lowest
    # continues through whole array
    # then switches with the index old lowest index 
    # in order to go through the whole array, get the length of the array
    # and increment one time until the length of the array is done 

    # one thing to save the value
    # two things to save the index

    for i in range(0, len(arr) -1):
        first_index = i
        counting_index = first_index
        current_min_elem = arr[i]
        second_index = counting_index
        # 👆need this to change dynamically to the first item in the unsorted portion of the array
        for elem in arr[i:]:
            if elem < current_min_elem:
                second_index = counting_index
                current_min_elem = elem
            counting_index += 1

        arr[second_index], arr[i] = arr[i], arr[second_index]
    return arr

    
    
        

print(selection_sort([3,6,4,1,2]))
    



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    pass
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
    pass

