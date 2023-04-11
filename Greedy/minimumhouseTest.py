from re import search

class Solution:
	def minimumBuckets(self, text: str) -> int:		
		return -1 if search('(^|H)H(H|$)', text) else text.count('H') - text.count('H.H')		
	
a = Solution()
street = "H..H"
#street = ".H.H."
#street = ".HHH."
#street = "........HHHH..."
print(a.minimumBuckets(street))


#a = '.H.H.H.H'
#print(a.count('H.H'))	
				
