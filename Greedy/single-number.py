from typing import List

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		seen_once = seen_twice = 0
		
		for num in nums:
			print('before', bin(num), bin(seen_once), bin(seen_twice))
			seen_once = ~seen_twice & (seen_once ^ num)
			seen_twice = ~seen_once & (seen_twice ^ num)
			print('after', bin(seen_once), bin(seen_twice))
		return seen_once
a = Solution()
print(a.singleNumber([2, 2, 3, 2]))


