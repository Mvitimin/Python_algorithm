#XL -> LX
#RX -> XR
class Solution:
	def canTransform(self, start: str, end: str) -> bool:
		if start.replace('X', '') != end.replace('X', ''):
			return False
		n = len(start)
		
		def move(s, si):
			while si < n and s[si] == 'X':
				si += 1
			return si
		
		i = move(start, 0)
		j = move(end, 0)
		
		# 'L' should be right or same from end index
		# 'R' should be left or same from end index
		while i < n and j < n:
			if start[i] == 'L' and i < j:
				break
			if start[i] == 'R' and i > j:
				break
			
			i = move(start, i + 1)
			j = move(end, j + 1)
				
		
		return i == len(start) and j == len(end)	
										
				
				
													
																		
a = Solution()
start = "RXXLRXRXL"; end = "XRLXXRRLX"	
start = "XXXLXXXXXX"; end = "XXXLXXXXXX"
start = "XXXXXLXXXX"; end = "LXXXXXXXXX"
start = "XRRXRX"; end = "RXLRRX"	
start = "XXRXLX RXXX"; end = "XXRLXX XXXR"	
#start = "p"; end = "LXXXXXXRRR"	
#start = "LXXLXRLXXL"; end = "XLLXRXLXLX"
print(a.canTransform(start, end))

					
															
				
			
