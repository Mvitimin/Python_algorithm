from typing import List

class Solution:
	def minmaxGasDist(self, stations: List[int], k: int) -> float:
		n = len(stations)
		def possible(dist):
			return sum(int((stations[i + 1] - stations[i]) / dist) for i in range(n - 1)) <= k		
		left, right = 0, 10**8
		while right - left > 1e-6:
			mid = (left + right) / 2.0
			if possible(mid):
				right = mid 
			else:
				left = mid
		return left		
				
				
		
		
a = Solution()
stations = [1,2,3,4,5,6,7,8,9,10]; k = 9
#stations = [23,24,36,39,46,56,57,65,84,98]; k = 1
#stations = [10,19,25,27,56,63,70,87,96,97]; k = 3
#stations = [13,15,20,31,46,49,51,52,67,87]; k =7
print(a.minmaxGasDist(stations, k))	
