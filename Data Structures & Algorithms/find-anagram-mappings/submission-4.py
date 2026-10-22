class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        result = []

        for i, n in enumerate(nums2):
            mappings[n] = i
        
        return [mappings[num] for num in nums1]