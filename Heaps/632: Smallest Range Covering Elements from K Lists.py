# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# difficulty: hard
# topics: array, hash table, greedy, sliding window, sorting, heap (priority queue)

# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

# priority queue solution
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]: 
        minHeap = []
        currMax = -float("inf")
        currStart, currEnd = 0, float("inf")
        k = len(nums)
        for i in range(k):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            currMax = max(currMax, nums[i][0])
        while len(minHeap) == k:
            n, numsIdx, listIdx = heapq.heappop(minHeap)
            if currMax-n < currEnd-currStart: currStart, currEnd = n, currMax
            listIdx += 1
            if listIdx == len(nums[numsIdx]): break
            heapq.heappush(minHeap, (nums[numsIdx][listIdx], numsIdx, listIdx))
            currMax = max(currMax, nums[numsIdx][listIdx])
        return [currStart, currEnd]
# at any moment, we need one element from each of the k lists
# to find the smallest range, we need to minimize the difference between the smallest and largest numbers chosen at each step
# we use a heap to keep track of the smallest element among the selected numbers
# we also keep track of the largest element among the selected numbers
# at each step, we extract the smallest element from the heap and push onto the heap the next smallest element from the same list
# after updating the heap, we check if the current range between the smallest and largest elements is smaller than the previous best range
# we repeat this until we can no longer add numbers from one of the lists to the heap

# time complexity: O(nlogk)
#     inserting into the heap takes O(logk) time
#     we insert all n numbers into the heap
# space complexity: O(k)
#     priority queue contains O(k) elements

# sliding window solution
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]: 
        allNums = []
        k = len(nums)
        for i in range(k):
            for x in nums[i]:
                allNums.append((x, i))
        allNums.sort()
        n = len(allNums)
        ans = [allNums[0][0], allNums[-1][0]]
        start = numMatches = 0
        listMatches = defaultdict(int)
        for end in range(n):
            listMatches[allNums[end][1]] += 1
            if listMatches[allNums[end][1]] == 1: numMatches += 1
            while numMatches == k:
                if ans[1]-ans[0] > allNums[end][0]-allNums[start][0]:
                    ans = [allNums[start][0], allNums[end][0]]
                listMatches[allNums[start][1]] -= 1
                if listMatches[allNums[start][1]] == 0: numMatches -= 1
                start += 1
        return ans
"""
# flatten nums into one sorted list of tuples, with first element representing value and second element representing list index
# use sliding window and keep track of represented lists in current window using a hash map
# check all windows ending at each index of merged list
# find smallest window range ending at that index that contains an element from all lists
      
# time complexity: O(nlogn)
#   sorting all numbers takes O(nlogn) time
#   traversing through all numbers and using sliding window takes O(n) time
# space complexity: O(n)
#   we create a list of all n elements
