import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_alpha_numeric_string = re.sub('[^0-9a-zA-Z]', '', s.lower())
        reverse_string = lower_alpha_numeric_string[::-1]
        return lower_alpha_numeric_string == reverse_string

print(Solution().isPalindrome("ab_a"))