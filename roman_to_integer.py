class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        summ = 0
        for c in inp:
            num = roman[s]
            if 3 * num < summ:
                summ = summ - num
            else:
                summ = summ + num

        return summ

if __name__ == '__main__':
    inp = "MCMXCIV"
    solution = Solution()
    val = solution.romanToInt(inp)
    print(val)




