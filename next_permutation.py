# https://leetcode.com/problems/next-permutation/discuss/804608/Python-Simple-Solution-Explained-(code-%2B-video
# Explanation https://www.youtube.com/watch?v=9xT2Xzlo4i4
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <= 2:
            return nums.reverse()
        pointer = length - 2

        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        if pointer == -1:
            return nums.reverse()

        for x in range(length - 1, pointer, -1):
            if nums[pointer] < nums[x]:
                nums[pointer], nums[x] = nums[x], nums[pointer]
                break

        nums[pointer + 1:] = reversed(nums[pointer + 1:])


if __name__ == '__main__':
    nums = [1, 2, 3]

    solution = Solution()
    solution.nextPermutation(nums)
