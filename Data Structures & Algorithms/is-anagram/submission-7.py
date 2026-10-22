class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        if len(t) != len(s):
            return False

        for c in t:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for c in s:
            if c not in freq or freq[c] == 0:
                return False
            freq[c] -= 1
        return True