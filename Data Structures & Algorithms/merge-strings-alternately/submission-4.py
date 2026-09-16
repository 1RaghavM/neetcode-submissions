class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0
        output = ""
        while first < len(word1) and second < len(word2):
            output += word1[first]
            output += word2[second]
            first, second = first + 1, second + 1
        output += word1[first:]
        output += word2[second:]
        return output