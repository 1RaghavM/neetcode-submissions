class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        check = {}
        for num in nums:
            if num not in check:
                check[num] = 1
            else:
                check[num] += 1

        max_unique = -1
        for key, val in check.items():
            if val == 1:
                max_unique = max(max_unique, key)
        return max_unique
        