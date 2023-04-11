

def minimumLoss(price):
	event = []
	for i, p in enumerate(price):
		event.append((p, i))
	
	event.sort(reverse=True)
	stack = []
	ans = float('inf')
	
	for p, i in event:
		while stack and stack[-1] < i:
			ans = min(ans, price[stack.pop()] - p)
		stack.append(i)
		
	return ans

price = [20, 15, 8, 2, 12]
price = [8, 2, 15, 20]
price = [5, 10, 3]
price = [20, 7, 8, 2, 5]
res = minimumLoss(price)
print(res)
