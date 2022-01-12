import re
from typing import List
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s

        def extend(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        ans = ''
        for i in range(len(s) - 1):
            ans = max(ans,
                      extend(i, i + 1),
                      extend(i, i + 2),
                      key=len)
        return ans


print(Solution().longestPalindrome("babad"))
