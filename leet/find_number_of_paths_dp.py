class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        print(dp)
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]

''' 
#back tracking pure O(2^ (m+n))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        init_pos = [0,0]
        fin_pos = [m-1, n-1]
        number_of_paths = 0


        def backtrack(pos, fin_pos):
            nonlocal number_of_paths
            if pos == fin_pos:
                number_of_paths += 1
                return
            
            #going down
            if pos[0]+1 <=fin_pos[0]:
                backtrack([pos[0]+1, pos[1]], fin_pos)

            #going right
            if pos[1]+1 <=fin_pos[1]:
                backtrack([pos[0], pos[1]+1], fin_pos)
            
            return

        backtrack(init_pos, fin_pos)
        #print(number_of_paths)
        return number_of_paths
'''
        

            

