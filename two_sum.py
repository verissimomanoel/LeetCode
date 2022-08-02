from typing import List


class Solution:
    def twoSumBest(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos1 = 0
        found = False
        while pos1 < len(nums):
            value = nums[pos1:pos1 + 1][0]
            pos2 = 0
            for num in nums:
                if pos2 == pos1:
                    pos2 += 1
                    continue

                total = value + num
                if total == target:
                    found = True
                    break

                pos2 += 1

            if found:
                break

            pos1 += 1

        return [pos1, pos2]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    weakest = solution.twoSumBest(nums, target)
    print(weakest)
