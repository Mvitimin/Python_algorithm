from typing import List
class Solution:
	def maxProfit(self, inventory: List[int], orders: int) -> int:
		ans, mod_val = 0, 10 ** 9 + 7
		inventory.append(0)
		inventory.sort(reverse=True)
	
		for i in range(len(inventory) - 1):
			if inventory[i] > inventory[i + 1]:
				if orders > (inventory[i] - inventory[i + 1]) * (i + 1):
					diff = (inventory[i] - inventory[i + 1])
					ans += (inventory[i] + inventory[i + 1] + 1) * diff * (i + 1) // 2
					orders -= diff * (i + 1)
				else:		
					q, r = divmod(orders, i + 1)
					ans += (inventory[i] * 2 - q + 1) * q * (i + 1) // 2
					ans += (inventory[i] - q) * r
					break			
		return ans % mod_val
			
a = Solution()

'''
inventory = [2,8,4,10,6]
orders = 20

'''
inventory = [2,5]
orders = 4

inventory = [3,5]
orders = 6

inventory = [1000000000]
orders = 1000000000

print(a.maxProfit(inventory, orders))
