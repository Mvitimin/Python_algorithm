class Solution:
	def sumGame(self, num: str) -> bool:
		n = len(num)
		mid = n // 2
		cnt = s = 0 
		for i, c in enumerate(num):
			if c == '?':
				cnt = (cnt - 1 if i < mid else cnt + 1) 
			else:
				s = (s + int(c) if i < mid else s - int(c))
		
		if cnt % 2 == 1:
			return True
		
		return not (cnt % 2 == 0 and s == (cnt // 2) * 9)
	
				
a = Solution()
num = "25??"
#num = "5023"
#num = "?3295???"
print(a.sumGame(num))			
		
				
			
