class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = []
        for i in range(n):
            nums += [i+1]
        #print(nums)
        res = []
        self.dfs(nums, '', res,1)
        res.sort()
        #print(res)
        return(res[k-1])


    def dfs(self, nums, path, res,sq):
        if not nums:
            res += [path]
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + str(nums[i]), res,sq)

        
