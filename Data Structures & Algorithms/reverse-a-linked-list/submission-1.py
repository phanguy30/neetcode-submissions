class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None

        # Just one while loop is needed!
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev