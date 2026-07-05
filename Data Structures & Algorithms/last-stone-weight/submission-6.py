class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = [-s for s in stones]
        
        heapq.heapify(result)
        while len(result) > 1:
            stone_x = heapq.heappop(result)
            stone_y = heapq.heappop(result)
            if stone_y > stone_x:
                heapq.heappush(result, stone_x - stone_y)
        
        result.append(0)
        return abs(result[0])
