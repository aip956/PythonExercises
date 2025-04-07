import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif num > pq[0]:
                heapq.heappushpop(pq, num) # Push and pop
        return pq[0]


if __name__ == '__main__':
    sol = Solution()
    var1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(sol.findKthLargest(var1, k1))
    var2 = [7, 10, 4, 3, 20, 15]
    k2 = 4
    print(sol.findKthLargest(var2, k2))