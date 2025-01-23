# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)  # Dummy head for result linked list
        current = dummy_head       # Pointer to build new list
        carry = 0                  # Initialize carry
        
        # Traverse both lists
        while l1 is not None or l2 is not None:
            # Get values from nodes or use 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10      # Update carry for next iteration
            current.next = ListNode(total % 10)  # Create new node for result
            
            # Move to next nodes in both lists
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        # If there's any carry left, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next     # Return the next node after dummy head
