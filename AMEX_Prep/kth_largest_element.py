class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse= True)
        return(nums[k - 1])

        # space complexity is O(1), time complexity is gonna be O(nlog(n))
        # how can we do better?

        import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [-elem for elem in nums]
        heapq.heapify(heap)
        for i in range(k-1): 
            heapq.heappop(heap)
        return -heapq.heappop(heap)

        #O(n log(k)) and O(n) space