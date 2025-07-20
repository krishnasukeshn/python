import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ''
        nums = range(1,n+1)
        print(nums)
        while len(nums)>0:
            fact = factorial(len(nums))
            comb_pernum = fact/len(nums)
            #print('comb_pernum: ' + str(comb_pernum))
            #print(float(3)/float(2))
            #print(k/comb_pernum)
            start_dig = int(math.ceil(float(k)/float(comb_pernum)))
            #print('start_diz: ' + str(start_dig))
            k = k % comb_pernum
            ans = ans + str(nums[start_dig-1])
            nums.pop(start_dig-1)
            #print('ans' + str(ans))
            #print(nums)
        return ans





        '''

        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        print(numbers)
        while n > 0:
            n -= 1
            # get the index of current digit
            print(divmod(k, math.factorial(n)))
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])
            print(numbers)

        return permutation
        '''







        '''
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

        '''
