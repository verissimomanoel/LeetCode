class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid

        # left > right
        return right

if __name__ == '__main__':
    x = 16

    solution = Solution()
    val = solution.mySqrt(x)
    print(val)