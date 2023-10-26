import heapq

def peekTopK(arr, k):
    topK = []

    if k <= 0 or k > len(arr):
        return topK

    # Create a max heap using a negative sign to reverse the order
    max_heap = [-x for x in arr]
    
    # Convert the list into a max heap
    heapq.heapify(max_heap)

    for i in range(k):
        if max_heap:
            topK.append(-heapq.heappop(max_heap))  # Negate the result to get the max value
        else:
            break

    return topK

# Example usage:
arr = [15, 13, 12, 10, 8, 9]
k = 5
topK = peekTopK(arr, k)
print(topK)  # Output: [15, 13, 12, 10, 9]
