from typing import List
import bisect
class Solution:
	def maxValue(self, events: List[List[int]], k: int) -> int:
		n = len(events)
		events.sort(key=lambda x : x[1])
		endTimes = [events[i][1] for i in range(n)]
		
		prev = {i : -1 for i in range(n)}
		dp = [[0] * (n + 1) for _ in range(k + 1)]
																						
		for i in range(1, n):
			idx = bisect.bisect_left(endTimes, events[i][0])
			prev[i] = idx - 1 if idx >= 0 else -1
			
		ans = 0
		for i in range(1, k + 1):
			for j in range(n):
				dp[i][j] = max(dp[i - 1][prev[j]] + events[j][2], dp[i - 1][j], dp[i][j - 1])
		
		return dp[k][n - 1]
						
a = Solution()
events = [[1,2,4],[3,4,3],[2,3,1]]; k = 2
events = [[1,2,4],[3,4,3],[2,3,10]]; k = 2
#events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]; k = 3
events = [[11,17,56],[24,40,53],[5,62,67],[66,69,84],[56,89,15]]; k = 2
#events = [[21,77,43],[2,74,47],[6,59,22],[47,47,38],[13,74,57],[27,55,27],[8,15,8]]; k = 4
#events = [[19,42,7],[41,73,15],[52,73,84],[84,92,96],[6,64,50],[12,56,27],[22,74,44],[38,85,61]]; k = 5
print(a.maxValue(events, k))				
				
			
		
		
						
			
			
			
