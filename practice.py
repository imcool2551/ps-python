class Solution:
    def reverseString(self, s) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


li = ["h", "e", "l", "l", "o"]
print(Solution().reverseString(li))
print(li)
