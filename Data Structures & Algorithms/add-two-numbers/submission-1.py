# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#It is recommended to perform this in O(1) space hence we can parse and store the variables as int. However, when it comes to the creation of the new linkedlist to return the value we run into a problem. We can reverse each list then store num1 and num2. Ten we add them, how do we create the linked list from that? Maybe reversing is not the way. We can add the values and carry on the integers by keeping track of pointer in our new linked list? I think i like that approach. Lets map it.
        remainder = 0 
        dummy = ListNode(0)
        tail = dummy 
        while l1 or l2 or remainder:
            total = remainder 
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next 
            remainder = total//10
            tail.next = ListNode(total%10)
            tail = tail.next 
        return dummy.next








