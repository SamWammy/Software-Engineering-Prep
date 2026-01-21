def find_min(arr):
    if not arr: 
        return 
    
    currMin= arr[0]

    for num in arr[1::]: 
        if num < currMin: 
            currMin = num
    return currMin

# Example: [3, 1, 4, 1, 5, 9] → 1

#Time: O(n), Space: O(1)
