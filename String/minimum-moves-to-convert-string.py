class Solution:
	def minimumMoves(self, s: str) -> int:
		moves = 0
		changed = list(s)
		n = len(changed)
		for i in range(n):
			if changed[i] == 'X':
				for j in range(i, min(n, i + 3)):
					changed[j] = 'O'
				moves += 1
		return moves	
					
a = Solution()
s = "XXX"
s = "XXOX"
s = "OOOO"
print(a.minimumMoves(s))
