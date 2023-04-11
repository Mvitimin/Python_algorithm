class Solution:
	def minimumBuckets(self, text: str) -> int:
		street = list(text)
		n = len(street)
		ans = 0
		for i in range(n):
			if street[i] == 'H':
				if text[i - 1:i] == '.' or text[i + 1:i + 2] == '.':
					if text[i + 1:i + 2] == '.' and text[i + 2:i + 3] == 'H': 
						street[i + 2:i + 3] = '*'
					street[i] = '*'
					ans += 1
				else: return -1
		return ans					
					
	
a = Solution()
street = "H..H"
#street = ".H.H."
#street = ".HHH."
#street = "........HHHH..."
print(a.minimumBuckets(street))
		
				
