class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:
		prev = [1 if 1 <= i <= k else 0 for i in range(target + 1)]  
		M = (10 ** 9 + 7)		
		for i in range(1, n):
			cur = [0] * (target + 1)	
			for j in range(1, target + 1):
				for p in range(1, min(j, k + 1)):
					if (j - p) > 0:
						cur[j] += (prev[j - p])
						cur[j] %= M
						
			prev = cur
		return prev[-1]
			
a = Solution()
n = 2; k = 6; target = 7
n = 30; k = 30; target = 500
print(a.numRollsToTarget(n, k, target))
