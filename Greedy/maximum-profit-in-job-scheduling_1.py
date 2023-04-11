from typing import List
class Solution:
	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		n = len(startTime)
		array = []
		dp = [0] * n
		for i in range(n):
			array.append((endTime[i], startTime[i], profit[i]))
		array.sort()
		
		def search(start):
			i, j = 0, n - 1
			while i <= j:
				mid = (i + j) // 2
				if start >= array[mid][0]:
					i = mid + 1 
				elif start < array[mid][0]:
					j = mid - 1	 	
			return j
				
		for i in range(n):
			end, start, p = array[i]
			index = search(start)	
			if 0 <= index < n:
				dp[i] = dp[index] + p
			else: dp[i] = p
			dp[i] = max(dp[i - 1], dp[i])
		return dp[-1]
		
a = Solution()
startTime = [1,2,3,3]; endTime = [3,4,5,6]; profit = [50,10,40,70]
startTime = [1,2,3,4,6]; endTime = [3,5,10,6,9]; profit = [20,20,100,70,60]
startTime = [1,1,1]; endTime = [2,3,4]; profit = [5,6,4]
startTime = [24,24,7,2,1,13,6,14,18,24];endTime=[27,27,20,7,14,22,20,24,19,27];profit = [6,1,4,2,3,6,5,6,9,8]
startTime = [6,24,45,27,13,43,47,36,14,11,11,12];endTime =[31,27,48,46,44,46,50,49,24,42,13,27];profit=[14,4,16,12,20,3,18,6,9,1,2,8]
print(a.jobScheduling(startTime, endTime, profit))	
			
			
