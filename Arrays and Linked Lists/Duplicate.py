### Problem Statement

#You have been given an array of `length = n`. The array contains integers from `0` to `n - 2`. 
#Each number in the array is present exactly once except for --------one number which is present twice-----------------. 
#Find and return this duplicate number present in the array

#**Example:**
#* `arr = [0, 2, 3, 1, 4, 5, 3]`
#* `output = 3` (because `3` is present twice)

#The expected time complexity for this problem is `O(n)` and the expected space-complexity is `O(1)`.


def duplicate(arr):
    Unique_sum = sum(set(arr))  #Unique Number sum
    actual_sum = sum(arr)       #actual sum of all numbers
    print(actual_sum - Unique_sum) # this will print the only duplicate number in array
