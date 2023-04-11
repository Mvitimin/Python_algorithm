from typing import List
import bisect

class Solution:
	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		n = len(startTime)
		events = []
		prev = {i : -1 for i in range(n)}
		dp = [0] * (n + 1)
		
		for i in range(n):
			events.append((startTime[i], endTime[i], profit[i]))
		
		events.sort(key = lambda x : x[1])
		endTime = [events[i][1] for i in range(n)]
		
		for i in range(n):
			idx = bisect.bisect_right(endTime, events[i][0])
			prev[i] = idx - 1 if 0 <= idx < n else -1	
		
		for i in range(n):
			dp[i] = max(dp[prev[i]] + events[i][2], dp[i - 1])
		
		return dp[n - 1]

	
a = Solution()
startTime = [1,2,3,3]; endTime = [3,4,5,6]; profit = [50,10,40,70]
#startTime = [1,2,3,4,6]; endTime = [3,5,10,6,9]; profit = [20,20,100,70,60]
#startTime = [1,1,1]; endTime = [2,3,4]; profit = [5,6,4]
print(a.jobScheduling(startTime, endTime, profit))	
