# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Cant use a seen arr but we can use a hash map i guess that will also track the frequency of each of the nodes. Cause we can have 2 nodes being unique in the path but have the same value which deems this algorithm useless and also take up extra space we dont need
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next 
            if fast == slow:
                return True 
        return False
