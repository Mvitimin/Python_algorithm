
def lilysHomework(arr):
	n = len(arr)
	t = [x for x in arr]
	sorted_arr = sorted(arr)
	reversed_arr = sorted(arr, reverse=True)
		
	if n <= 2:
		return 0
	
	def check(p):
		arr = [x for x in t]
		maps = {}
		for i in range(n):
			maps[arr[i]] = i
		swap = 0	
		for i in range(n):
			if arr[i] != p[i]:
				idx = maps[p[i]]
				maps[p[i]] = i
				maps[arr[i]] = idx
				arr[idx], arr[i] = arr[i], arr[idx]
				swap += 1	
		return swap
	return min(check(sorted_arr), check(reversed_arr))
	
	
arr = [8, 5, 1, 3, 6, 4, 2]
arr = [7, 15, 12, 3]
arr = [3, 4, 2, 5, 1]

res = lilysHomework(arr)		
print(res)		
		
			
		
	
	
