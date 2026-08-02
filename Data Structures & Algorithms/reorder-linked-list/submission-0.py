# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#My though is go through the list once and append the nodes in the list, and then pop them and change the next values of the current head one by one. I didnt understand the problem correctly. I need t
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1) we find the middle of the list 
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev 
        while second:
            tmp1,tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1
            first, second = tmp1,tmp2
            
        