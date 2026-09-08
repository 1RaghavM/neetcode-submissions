class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}

        for i, n in enumerate(numbers):
            check[n] = i
        
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in check and check[diff] != i:
                return [i + 1, check[diff] + 1]
        return []
        
