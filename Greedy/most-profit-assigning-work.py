from typing import List
class Solution:
	def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
		event = []
		n = len(difficulty)
		for i in range(n):
			event.append((difficulty[i], profit[i]))	
		event.sort(reverse=True)
		worker.sort()
		
		max_val = 0
		ans = 0	
		for w in worker:
			while event and event[-1][0] <= w:
				d, p = event.pop()
				max_val = max(max_val, p)
			ans += max_val
		return ans

a = Solution()
difficulty = [2,4,6,8,10]; profit = [10,20,30,40,50];worker = [4,5,6,7]
difficulty = [85,47,57]; profit = [24,66,99]; worker = [40,25,25]
difficulty = [64,88,97]; profit = [53,86,89]; worker = [98,11,6]
print(a.maxProfitAssignment(difficulty, profit, worker))
