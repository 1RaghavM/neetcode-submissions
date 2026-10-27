class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {}
        start = 0
        output = 0

        for i, n in enumerate(keyboard):
            indices[n] = i

        for c in word:
            j = indices[c]
            output += abs(start - j)
            start = indices[c]
        return output
