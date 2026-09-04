class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        output = []
        for i,n in enumerate(nums2):
            table[n] = i
        
        for num in nums1:
            output.append(table[num])
        
        return output
        
