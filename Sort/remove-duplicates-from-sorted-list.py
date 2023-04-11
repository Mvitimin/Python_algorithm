
from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		
		cur = head
		
		while cur:
			if cur.next and cur.val == cur.next.val:
				cur.next = cur.next.next	
			else: cur = cur.next 
		return head
			

def makeList(arr):
	root = node = ListNode()
	for num in arr:
		node.next = ListNode(num)
		node = node.next
	return root.next
			
def printNode(node):
	while node:
		print(node.val, end='->')
		node = node.next
	print()
	
																		
a = Solution()
head = [1, 1, 2]
head = [1,1,2,3,3]
#head = [1, 4, 5, 7, 7, 7]
node = makeList(head)
printNode(a.deleteDuplicates(node))			
			

