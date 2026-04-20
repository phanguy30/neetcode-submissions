"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy_nodes = {None: None}

        curr = head
        while curr:
            copy_nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            curr_copy = copy_nodes[curr]
            curr_copy.next = copy_nodes[curr.next]
            curr_copy.random = copy_nodes[curr.random]
            curr = curr.next
        
        return copy_nodes[head]
        