# https://redquark.org/leetcode/0022-generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Resultant list
        result = []
        # Recursively generate parentheses
        self.generate(result, "", 0, 0, n)
        return result

    def generate(self, result: List[str], s: str, _open: int, close: int, n: int):
        # Base condition
        if _open == n and close == n:
            result.append(s)
            return
        # If the number of _open parentheses is less than the given n
        if _open < n:
            self.generate(result, s + "(", _open + 1, close, n)
        # If we need more close parentheses to balance
        if close < _open:
            self.generate(result, s + ")", _open, close + 1, n)

if __name__ == '__main__':
    n = 3
    solution = Solution()
    result = solution.generateParenthesis(n)
    print(result)