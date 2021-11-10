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

# diffrent Solution

def Add_One(arr):
    borrow = 1
    # Traverse in reverse direction starting from the end of the list
    for i in range(len(arr), 0, -1):

        # The "digit" denotes the updated Unit, Tens, and then Hunderd  position iteratively
        digit = borrow + arr[i - 1]

        """
        The "borrow" will be carried to the next left digit
        If the digit is between 0-9, borrrow will be 0.
        If digit is 10, then the borrow will be 1.
        """
        # The "//" is a floor division operator
        borrow = digit // 10

        if borrow == 0:
            # Update the arr[i - 1] with the updated digit, and quit the FOR loop.
            arr[i - 1] = digit
            break
        else:
            # Update the arr[i - 1] with the remainder of (digit % 10)
            arr[i - 1] = digit % 10

    # Prepend the final "borrow" to the original array.
    arr = [borrow] + arr
    position = 0
    while arr[position] == 0:
        position += 1

    return arr[position:]
