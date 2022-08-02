from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for line in accounts:
            total = sum(line)
            if total > richest:
                richest = total

        return richest


if __name__ == '__main__':
    accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    solution = Solution()
    weakest = solution.maximumWealth(accounts)
    print(weakest)
