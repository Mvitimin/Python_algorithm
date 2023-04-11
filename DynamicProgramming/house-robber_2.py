from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		a = b = 0
		
		for i in range(n):
			a, b = b, max(a + nums[i], b)
		return b
			
a = Solution()
nums = [2, 9, 8, 1, 7, 3]
#print(a.rob(nums))


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		

a = Node(3)
b = Node(5)
c = Node(6)
a.next = b
b.next = c

a, a.next = b, None

print(a.val)
print(a.next)

t = [1, 2, 3, 4]

t, t[1] = [4, 5], 6
print(t)
