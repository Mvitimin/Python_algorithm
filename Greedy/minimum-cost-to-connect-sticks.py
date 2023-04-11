from typing import List
import heapq

class Solution:
	def connectSticks(self, sticks: List[int]) -> int:
		if len(sticks) <= 1:
			return 0
		
		ans = 0
		heapq.heapify(sticks)
		while sticks:
			if len(sticks) <= 1:
				return ans
			a, b = heapq.heappop(sticks), heapq.heappop(sticks)
			stick = a + b
			heapq.heappush(sticks, stick)
			ans += stick
		return ans


a = Solution()
sticks = [1,8,3,5]
sticks = [2,4,3]
print(a.connectSticks(sticks))
