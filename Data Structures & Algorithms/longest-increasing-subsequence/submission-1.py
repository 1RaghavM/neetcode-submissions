from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            k = bisect_left(tails, num)
            if k == len(tails):
                tails.append(num)
            else:
                tails[k] = num
        return len(tails)