from typing import List
import heapq
class Solution:
	def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
		n = len(startTime)
		array = []
		for i in range(n):
			array.append((startTime[i], endTime[i], profit[i]))
		array.sort()
		
		heap = [(-array[0][2], 0, 1)]
		ans = 0
		while heap:
			print(heap)
			p, index, next = heapq.heappop(heap)
			p = -p
			ans = max(p, ans)
			if index >= n: break
			if next >= n: continue
			start, end = array[index][0], array[index][1]
			if max(start, array[next][0]) < min(end, array[next][1]):
				heapq.heappush(heap, (-(p + array[next][2] - array[index][2]), next, next + 1))
			else:
				heapq.heappush(heap, (-(p + array[next][2]), next, next + 1))
			heapq.heappush(heap, (-p, index, next + 1))	
			
		return ans
		
a = Solution()
startTime = [1,2,3,3]; endTime = [3,4,5,6]; profit = [50,10,40,70]
startTime = [1,2,3,4,6]; endTime = [3,5,10,6,9]; profit = [20,20,100,70,60]
startTime = [1,1,1]; endTime = [2,3,4]; profit = [5,6,4]
startTime = [24,24,7,2,1,13,6,14,18,24];endTime=[27,27,20,7,14,22,20,24,19,27];
profit = [6,1,4,2,3,6,5,6,9,8]
print(a.jobScheduling(startTime, endTime, profit))

	
			
			

