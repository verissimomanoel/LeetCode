from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        triplets = []

        nums = sorted(nums)
        for i in range(0, len(nums) - 2):
            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                sum_value = nums[i] + nums[lower] + nums[upper]

                if sum_value == 0:
                    triplets.append((nums[i], nums[lower], nums[upper]))
                    lower += 1
                elif sum_value < 0:
                    lower += 1
                else:
                    upper -= 1

        return list(set(triplets))


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    solution = Solution()
    val = solution.threeSum(nums)
    print(val)
