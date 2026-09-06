class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = {}

        for num in nums:
            if num not in output:
                output[num] = 1
            else:
                output[num] += 1
        
        for key, val in output.items():
            if val > len(nums) / 2:
                return key
            
    
