#### Problem Statement

# You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list. 

#**Example 1:**
#* `input = [1, 2, 3]`
#* `output = [1, 2, 4]`

def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    idx=list(range(len(arr)))
    powers=list(range(len(arr)-1,-1,-1))
    total=0
    for i,p in zip(idx,powers):
        total += arr[i] * (10**p)

    last = total+1
    tab = [int(a) for a in str(last)]
    return tab
    
 
