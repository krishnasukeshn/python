class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tot = 0 
        res= nums[0]
        for x in nums:
            if tot< 0:
                tot =0
            tot = tot + x
            res = max(res, tot)
        return res
            
