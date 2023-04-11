from typing import List

class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		min_val = min(arr)
		max_val = max(arr)
		
		
		counter =  [0] * (max_val - min_val + 1)
		answer = []
		
		# distinct integers !!
		for num in arr:
			counter[num - min_val] = 1
			
		
		diff = max_val - min_val
		
		prev = 0
		
		print(counter)
		for curr in range(1, max_val - min_val + 1):
			if counter[curr] == 0: continue
			
			if curr - prev == diff:
				answer.append([prev + min_val, curr + min_val])
			elif curr - prev < diff:
				answer = [[prev + min_val, curr + min_val]]
				diff = curr - prev
			prev = curr
		
		return answer
		
arr = [4,2,1,3]
a = Solution()
print(a.minimumAbsDifference(arr))
