from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def length(self, head: Optional[ListNode]) -> int:
		p = head; n = 0	
		while p:
			n += 1
			p = p.next
		return n	
							
	def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
					
		stack = []
		l = self.length(head)
		root = ListNode()
		root.next = head
		p = root
		n = 0
		while p:
			if n in [k - 1, l - k]:
				stack.append(p)	
			n += 1	
			p = p.next
		if len(stack) < 2: return head
		
		first, second = stack[0].next, stack[1].next
		stack[0].next, stack[1].next = second, first
		first.next, second.next = second.next, first.next
		
		return root.next


def makeList(arr):
	root = ListNode()
	p = root 
	for n in arr:
		p.next = ListNode(n)
		p = p.next
	return root.next

def printNode(node):
	while node:
		print(node.val, end='->')
		node = node.next
	print()
	


head = [1,2,3]; k = 2	
head = [7,9,6,6,7,8,3,0,9,5]; k = 5
a = Solution()
node = a.swapNodes(makeList(head), k)
printNode(node)		
		
		

