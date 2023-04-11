class Solution:
	def crackSafe(self, n: int, k: int) -> str:
		
		visited = set()
		ans = ''
		def solve(pwd):		
			nonlocal ans
			if len(visited) == (k ** n + n - 1):
				ans = pwd
				return True
			l = len(pwd)
			for i in range(k):
				typed = pwd[max(l - n + 1, 0):] + str(i)
				if typed not in visited:
					visited.add(typed)
					if solve(pwd + str(i)): 
						return True
					visited.remove(typed)
			return False
		solve('')
		return ans


a = Solution()
n = 1; k = 2
n = 2; k = 2
print(a.crackSafe(n, k))
