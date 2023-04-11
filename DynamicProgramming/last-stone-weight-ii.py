from typing import List
class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		n = len(stones)
		total = sum(stones)
		end, start = total // 2, min(stones)
		dp = [False] * (end + 1)
		dp[0] = True
		for s in stones:
			for i in range(end, start - 1, -1):
				if i >= s and dp[i - s]:
					dp[i] = True
		for i in range(end, -1, -1):
			if dp[i]:
				return total - i * 2

a = Solution()
stones = [2,7,4,1,8,1]
stones = [31,26,33,21,40]
print(a.lastStoneWeightII(stones))
