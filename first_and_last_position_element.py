# https://www.tutorialspoint.com/find-first-and-last-position-of-element-in-sorted-array-in-python
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        low = 0
        high = len(nums)
        while low < high:
            mid = int(low + (high - low) // 2)
            if nums[mid] == target:
                high = mid
                res[0] = mid
                res[1] = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if res[0] == -1:
            return res

        low = res[0] + 1
        high = len(nums)

        while low < high:
            mid = int(low + (high - low) // 2)
            if nums[mid] == target:
                low = mid + 1
                res[1] = mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return res


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)
