#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s = '', open = 0, close = 0):
            if len(s) == 2*n:
                res.append(s)
            if open < n:
                backtrack(s + '(', open + 1, close)
            if close < open:
                backtrack(s + ')', open, close+1)

        backtrack()
        return res

