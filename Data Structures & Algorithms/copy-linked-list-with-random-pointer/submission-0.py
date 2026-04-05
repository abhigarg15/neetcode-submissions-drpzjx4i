"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.mp = {None:None}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        if head in self.mp:
            return self.mp[head]

        copy = Node(head.val)
        self.mp[head] = copy
        copy.next = self.copyRandomList(head.next)

        copy.random = self.mp[head.random]        

        return copy