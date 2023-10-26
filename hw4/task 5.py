def kthSmallestPrimeFraction(arr, k):
    low, high = 0.0, 1.0
    
    while high - low > 1e-9:
        mid = (low + high) / 2
        count, maxFraction = 0, 0.0
        j = 1
        
        for i in range(len(arr) - 1):
            while j < len(arr) and arr[i] > mid * arr[j]:
                j += 1
            count += len(arr) - j
            if j < len(arr):
                maxFraction = max(maxFraction, arr[i] / arr[j])
        
        if count == k:
            return [arr[i], arr[j - 1]]
        elif count < k:
            low = mid
        else:
            high = mid
    
    return [arr[i], arr[j - 1]]

# Example usage:
arr1 = [1, 2, 3, 5]
k1 = 3
print(kthSmallestPrimeFraction(arr1, k1))  # Output: [2, 5]

arr2 = [1, 7]
k2 = 1
print(kthSmallestPrimeFraction(arr2, k2))  # Output: [1, 7]
