class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in magazine:
            ransomNote = ransomNote.replace(c, '')

        return len(ransomNote) == 0


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"

    solution = Solution()
    val = solution.canConstruct(ransomNote, magazine)
    assert val == True
