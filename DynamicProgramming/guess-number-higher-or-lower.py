# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
	def guessNumber(self, n: int) -> int:		
		start, end = 1, n
		while start <= end:
			mid = start + (end - start) // 2
			print(mid)
			if guess(mid) == -1:
				start = mid + 1
			elif guess(mid) == 1:
				end = mid - 1
			else:
				return mid 
		return start

'''
class Solution:
	def guessNumber(self, n: int, pick: int) -> int:
		def guess(num: int):
			if num > pick: return 1 
			elif num < pick: return -1
			else: return 0
		
		start, end = 1, n
		while start <= end:
			mid = start + (end - start) // 2
			if guess(mid) == -1:
				start = mid + 1
			elif guess(mid) == 1:
				end = mid - 1
			else:
				return mid 	
'''		
			
					
a = Solution()
n = 10; pick = 6
n = 2; pick = 2
print(a.guessNumber(n, pick))

