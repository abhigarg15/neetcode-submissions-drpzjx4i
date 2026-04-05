# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ll = []
        for lst in lists:
            while lst:
                ll.append(lst.val)
                lst = lst.next

        ll.sort()

        dummy = ListNode()
        curr = dummy

        for i in ll:
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next