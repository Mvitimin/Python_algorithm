class Solution:
	def alphabetBoardPath(self, target: str) -> str:
		sr, sc, ans = 0, 0, ''
		
		for char in target:
			offset = ord(char) - ord('a')
			dr, dc = offset // 5, offset % 5
			
			if char == 'z' and sc != 0:
				dr -= 1
						
			if sr > dr:
				ans += 'U' * (sr - dr)
			if sr < dr:
				ans += 'D' * (dr - sr)
			if sc < dc:
				ans += 'R' * (dc - sc)
			if sc > dc:
				ans += 'L' * (sc - dc)
				
			if char == 'z' and dr == 4:
				ans += 'D'
				dr += 1
			
			ans += '!'
			sr, sc = dr, dc
		return ans 

				
a = Solution()
#target = "zdz"
#target = "zz"
target = "buzz"
print(a.alphabetBoardPath(target))
