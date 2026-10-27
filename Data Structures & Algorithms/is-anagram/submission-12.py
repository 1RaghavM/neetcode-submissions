class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(t)

        if len(s) != len(t):
            return False

        for c in s:
            if c in freq and freq[c] != 0:
                freq[c] -= 1
            else:
                return False
        return True
