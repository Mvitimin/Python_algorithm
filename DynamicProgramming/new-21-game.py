class Solution:
	def new21Game(self, n: int, k: int, maxPts: int) -> float:
		if k == 0:
			return 1
		dp = [0.0] * (n + 1)
		dp[0] = 1.0
		pre_sum = 1.0
		for i in range(1, n + 1):
			dp[i] = pre_sum / maxPts
			if i < k:
				pre_sum += dp[i]
			if 0 <= i - maxPts < k:
				pre_sum -= dp[i - maxPts]
		return sum(dp[k:])
		
		
a = Solution()
n = 10
k = 1
maxPts = 10

'''
n = 6
k = 1
maxPts = 10
'''
print(a.new21Game(n, k, maxPts))
