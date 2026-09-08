class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        output = []

        for num in nums:
            if num not in check:
                check[num] = 1
            else:
                check[num] += 1
        
        check_tu = []
        for key, value in check.items():
            check_tu.append((value, key))
        check_tu.sort(reverse=True)
        
        for i in range(k):
            output.append(check_tu[i][1])
        return output
