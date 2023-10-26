def findClosestElements(arr, k, x):
    # Binary search to find the index of the closest element to x
    left, right = 0, len(arr) - 1
    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1
    
    # Initialize result list with elements from arr[left:right+1]
    result = arr[left:right+1]
    
    # Sort the result in ascending order
    result.sort()
    
    return result

# Example usage:
arr1 = [1, 2, 3, 4, 5]
k1 = 4
x1 = 3
print(findClosestElements(arr1, k1, x1))  # Output: [1, 2, 3, 4]

arr2 = [1, 2, 3, 4, 5]
k2 = 4
x2 = -1
print(findClosestElements(arr2, k2, x2))  # Output: [1, 2, 3, 4]
