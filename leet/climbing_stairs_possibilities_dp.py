#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 if i == 0 else (2 if  i == 1 else 0) for i in range(n)]
        if  n < 3:
            return dp[n-1]
        else:
            for x in range(2,n):
                dp[x] = dp[x-1] + dp[x-2]
            return dp[n-1]

        
