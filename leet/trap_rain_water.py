class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        left = []
        for x in height:
            max_l = max(max_l,x)
            left.append(max_l)
        #print(left)
        max_r = 0
        right = []
        for x in height[::-1]:
            max_r = max(max_r, x)
            right.append(max_r)
        right = right[::-1]
        #print(right)

        trap_wat = 0
        for x in range(len(right)):
            trap_wat = (min(left[x], right[x]) -height[x]) +trap_wat
        #print(trap_wat)
        return trap_wat

