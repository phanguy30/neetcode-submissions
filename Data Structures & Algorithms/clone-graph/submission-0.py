from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # Map original nodes to their respective clones
        old_to_new = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                # If we haven't seen this neighbor, clone it and add to queue
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Link the same corresponding neighbors to the clone
                old_to_new[current].neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]