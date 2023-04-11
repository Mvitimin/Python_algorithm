class Solution:
	def checkRecord(self, n: int) -> int:	
		MODULO = 10 ** 9 + 7
		if n == 1:
			return 3
		
		noAendP, noAendL, noAendLL = 1, 1, 0
		endP, endA, endL, endLL = 1, 1, 1, 0 

		for i in range(1, n):
			endP, endL, endA, endLL = (endP + endL + endA + endLL) % MODULO, (endP + endA) % MODULO, (noAendP + noAendL + noAendLL) % MODULO, endL
			
			noAendP, noAendL, noAendLL = (noAendP + noAendL + noAendLL) % MODULO, noAendP, noAendL
			
		return (endP + endL + endA + endLL) % MODULO
		
a = Solution()
n = 2
n = 10101
#n = 1
print(a.checkRecord(n))
