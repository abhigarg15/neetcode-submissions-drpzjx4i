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
        mp = {None:None}

        curr = head
        while curr:
            newList = Node(curr.val)
            mp[curr] = newList
            curr = curr.next

        curr = head
        while curr:
            newList = mp[curr]
            newList.next = mp[curr.next]
            newList.random = mp[curr.random]
            curr = curr.next

        return mp[head]