from typing import List


# https://dev.to/seanpgallivan/solution-letter-combinations-of-a-phone-number-1n91

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_characters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        lenD, ans = len(digits), []
        if digits == "" : return []

        def bfs(pos: int, st: str):
            if pos == lenD:
                ans.append(st)
            else:
                letters = map_characters[digits[pos]]
                for letter in letters:
                    bfs(pos + 1, st + letter)

        bfs(0, "")
        return ans


if __name__ == '__main__':
    digits = "23"

    solution = Solution()
    val = solution.letterCombinations(digits)
    print(val)
