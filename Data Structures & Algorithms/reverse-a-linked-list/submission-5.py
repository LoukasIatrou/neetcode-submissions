# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#first we want to initialise the two pointers we will use to iterate through the arr 
        prev, curr = None, head
        while curr:
            temp = curr.next 
            curr.next =prev
            prev = curr
            curr= temp 
        return prev