from typing import List
import collections

class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		ans = []
		
		nums.sort()
		
		def solve(stack, map):
			if len(stack) == len(nums):
				ans.append(stack[::])
				return 
			
			for i, num in enumerate(nums):
				if len(map[num]) <= 0 or map[num][-1] < i:
					stack.append(nums[i])
					map[num].append(i)
					solve(stack, map)
					stack.pop()
					map[num].pop()
				i = (i + 1) % len(nums)
			
		map = collections.defaultdict(list)
		solve([], map)
		
		return ans
		
a = Solution()
nums = [1, 1, 2]
#nums = [1,2,3]
nums = [2, 1, 1]
print(a.permuteUnique(nums))
