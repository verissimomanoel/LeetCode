# https://levelup.gitconnected.com/valid-parentheses-python-8374c1612821#:~:text=Given%20a%20string%20s%20containing,the%20same%20type%20of%20brackets.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in dict.keys():
                stack.append(c)
            else:
                if not stack:
                    return False

                a = stack.pop()
                if c != dict[a]:
                    return False

        return stack == []

if __name__ == '__main__':
    # s = "([)]"
    # s = "()"
    s = "()[]{}"
    # s = "(]"
    # s = "{[]}"

    solution = Solution()
    val = solution.isValid(s)
    print(val)