from typing import List

class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		n = len(stones)
		s = sum(stones)
		l = s // 2 + 1
		dp = [False] * (l)
		dp[0] = True
		ans = 0
		
		for i in range(n):
			tmp = [dp[k] for k in range(l)]
			for j in range(l):
				if j - stones[i] >= 0 and dp[j - stones[i]]:
					tmp[j] = True
			dp = tmp
			
		for i in range(l - 1, -1, -1):
			if dp[i]:
				ans = s - i * 2
				break
		return ans
				
											
a = Solution()
stones = [2, 7, 4, 1, 8, 1]
stones = [1,2,4,8,16,32,64,12,25,51]
stones = [53,54,3,61,67]
stones = [31,26,33,21,40]
stones = [3,3,6,4,8,8]
stones = [1, 2]
print(a.lastStoneWeightII(stones))						


