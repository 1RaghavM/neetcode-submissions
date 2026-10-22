class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        result = []

        for i, n in enumerate(nums2):
            mapping[n] = i
        
        for num in nums1:
            result.append(mapping[num])
        
        return result