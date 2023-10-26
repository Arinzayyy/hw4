import collections
import heapq

def kMostFrequent(nums, k):
    # Step 1: Count the frequency of elements
    freq_dict = collections.Counter(nums)
    
    # Step 2: Create a min-heap to store elements along with their frequencies
    min_heap = []
    
    # Step 3 and 4: Push elements into the min-heap and maintain the size at k
    for num, freq in freq_dict.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Step 5 and 6: Extract elements from the min-heap
    result = [num for freq, num in min_heap]
    
    return result

# Example usage:
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(kMostFrequent(nums1, k1))  # Output: [1, 2]

nums2 = [1]
k2 = 1
print(kMostFrequent(nums2, k2))  # Output: [1]
