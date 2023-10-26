from collections import deque

def shortestSubarrayWithSumAtLeastK(nums, k):
    n = len(nums)
    minLength = float('inf')
    sumArray = [0] * (n + 1)
    monoQueue = deque()
    
    for i in range(n):
        sumArray[i + 1] = sumArray[i] + nums[i]
    
    for i in range(n + 1):
        while monoQueue and sumArray[i] - sumArray[monoQueue[0]] >= k:
            minLength = min(minLength, i - monoQueue.popleft())
        while monoQueue and sumArray[i] <= sumArray[monoQueue[-1]]:
            monoQueue.pop()
        monoQueue.append(i)
    
    return minLength if minLength != float('inf') else -1

# Example usage:
nums1 = [1]
k1 = 1
print(shortestSubarrayWithSumAtLeastK(nums1, k1))  # Output: 1

nums2 = [1, 2]
k2 = 4
print(shortestSubarrayWithSumAtLeastK(nums2, k2))  # Output: -1

nums3 = [2, -1, 2]
k3 = 3
print(shortestSubarrayWithSumAtLeastK(nums3, k3))  # Output: 3
