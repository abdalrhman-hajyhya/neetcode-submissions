# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def sumOfLinkedList(self, head):
        current = head
        sumOfLinkedList = 0
        multi = 1
        while current:
            sumOfLinkedList += current.val * multi
            multi *= 10
            current = current.next 
        return sumOfLinkedList

    def flipLinkedList(self, head):
        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumOfL1 = self.sumOfLinkedList(l1)
        sumOfL2 = self.sumOfLinkedList(l2)

        result = sumOfL1 + sumOfL2
        prev = None
        if result == 0:
            return ListNode(0,None)
        while result > 0:
            newNode = ListNode(result % 10)
            newNode.next = prev
            prev = newNode
            result = result // 10
        return self.flipLinkedList(prev)
            
        

         
        