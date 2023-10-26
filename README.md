# hw4
Approach 1

Create a dictionary (hash map) to count the frequency of each element in the nums array.

Traverse through the nums array and populate the dictionary with the frequency counts.

Create a min-heap (priority queue) to keep track of the k most frequent elements. You will store elements in the heap along with their frequencies.

Traverse through the dictionary and push the elements along with their frequencies into the min-heap. If the size of the min-heap exceeds k, pop the element with the lowest frequency to maintain the heap's size at k.

After processing all the elements in the dictionary, the min-heap will contain the k most frequent elements.

Extract the elements from the min-heap and add them to a result list.

The time complexity of the code I provided is O(n log k)


Approach 2

Perform a binary search to find the index i in the sorted array arr such that arr[i] is either equal to x or the closest integer to x.

Initialize two pointers, left and right, to expand outwards from index i. Initially, set left = i and right = i + 1.

While k > 0, repeatedly choose the closer of the elements at arr[left] and arr[right] to x and add it to the result list. Then, move the corresponding pointer left or right accordingly.

Continue this process until k elements are added to the result list.

Sort the result list in ascending order and return it.


Approach 3


Convert the max heap into a max-heap-like structure by negating all elements in the array. This effectively reverses the order of elements, turning them into a min-heap-like structure.

Use the heapq module (Python's built-in heap library) to create a heap from the modified array.

Extract the top k elements from the heap. Since the heap is a min-heap with the modified values, you will get the largest k elements in the original max heap.

Negate the results to revert them to their original values.

The time complexity is dominated by O(k * log n).


Approach 4

Initialize variables: minLength to store the minimum length subarray found so far, sumArray to track the cumulative sum of elements, and a deque (monoQueue) to maintain a non-increasing order of elements' indices.

Iterate through the nums array, and at each step, update the sumArray by adding the current element's value.

While sumArray is greater than or equal to k, pop elements from the left of the deque and update the minLength. These popped elements correspond to subarrays with a sum at least k. Continue this process until sumArray is no longer greater than or equal to k.

Finally, return minLength if it has been updated during the iteration; otherwise, return -1.



Approach 5

Initialize two variables, low and high, representing the minimum and maximum possible fractions in the range [0, 1] (since the smallest fraction is 1/arr[-1], and the largest is 1/1).

Perform a binary search between low and high to find the kth smallest fraction. In each iteration, calculate the mid-point mid between low and high and count how many fractions in the array are less than or equal to mid using a two-pointer approach.

If the count is greater than or equal to k, update high to mid, indicating that the kth smallest fraction is between low and mid. Otherwise, update low to mid, indicating that the kth smallest fraction is between mid and high.

Repeat the binary search until low is sufficiently close to high, and return the fraction low as the kth smallest prime fraction.

The overall time complexity is O(log(max_prime) * n)
