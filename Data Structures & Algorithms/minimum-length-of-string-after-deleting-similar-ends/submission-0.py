class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and c == s[left]:
                left += 1
            while left <= right and c == s[right]:
                right -= 1
        return right - left + 1
