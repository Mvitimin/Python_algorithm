
class Solution:
	def confusingNumberII(self, n: int) -> int:
		k = str(n)
		l = len(k)
		nums = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
	
		def find(i):
			ans = 0
			if i == l:
				return 1
			for num in nums:
				if k[i] > num:
					ans += 5 ** (l - i - 1) # 5: the number of digits (0, 1, 6, 8, 9)
				elif k[i] == num:
					ans += find(i + 1)
			return ans
					
		
		# find(0) includes 0 so minus 1 (because the range starts from 1)
		# pal: the number of palindromes
		ans, pal = find(0) - 1, 0	
		
		
		
		# O((5 ** l//2) * l)
		def findPalindrome(t):
			nonlocal pal
			if t and (len(t) > l or int(t) > n): 
				return
			if t and t[0] != '0':
				pal += 1	
			for num in nums:
				findPalindrome(num + t + nums[num])
		
		for num in ['0', '1', '8']:
			findPalindrome(num) # ex) 808, 619 
		findPalindrome('') # ex) 11, 88, 69, 9696
		return ans - pal
