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
        '''
#Biggest challenge is to ensure we point to the dummy nodes and not the original list nodes. Thoughtprocess: I can create n dummy nodes and iterate through the original list and point the dummy nodes to the corresponding original nodes. 
        dummy = p1 = Node(0)
        curr = head 
        while curr:
#We work on the current node before moving on to the next one. We should be initialising a new dummy node at the end of the while to be ready for the next pointer 
            p1 = Node(curr.val)
            p1.next = Node(curr.next)
            p1.random = Node(curr.random)
            curr = curr.next 
            p1 = p1.next 
        return head 
        '''
# This solution isnt valid. I should find a way to store only the value and not the next pointers as its there where a mistake is made. Potentially a double hashmap solution, one tracking the next and one the random and then work through the double hash map. This keeps O(n) for both space and time complexity as required. However it is hinted that there is a better solution. Lets work through this iteration and we see\
        old_to_new = {}
        curr = head
        if not head:
            return head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next 
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]
