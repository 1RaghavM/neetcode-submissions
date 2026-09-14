class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i, n in enumerate(nums):
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for key, value in freq.items():
            if value >= len(nums) / 2:
                return key