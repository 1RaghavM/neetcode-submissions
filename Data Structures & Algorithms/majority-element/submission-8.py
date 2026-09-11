class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = {}

        for num in nums:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
        
        for key, value in check.items():
            if value > len(nums) / 2:
                return key