class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}

        if len(s) != len(t):
            return False

        for c in t:
            if c in check:
                check[c] += 1
            else:
                check[c] = 1
        
        
        for c in s:
            if c not in check or check[c] == 0:
                return False
            else:
                check[c] -= 1
        return True
                