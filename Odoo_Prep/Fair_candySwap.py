class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        target = (sum(aliceSizes) - sum(bobSizes) )/2

        a = set(aliceSizes)
        for b in set(bobSizes):
            if target+ b in a: 
                return [target+b,b]
