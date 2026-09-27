# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        ar1=[]
        ar2=[]
        total=[]
        while l1:
            ar1.append(l1.val)
            l1=l1.next
        ar1.reverse()
        while l2:
            ar2.append(l2.val)
            l2=l2.next
        ar2.reverse()
        num1 = int("".join(map(str, ar1)))
        num2 = int("".join(map(str, ar2)))
        t=num1+num2
        t=str(t)[::-1]
        head = ListNode(int(t[0]))
        current = head
        for digit in t[1:]:
            current.next = ListNode(int(digit))
            current = current.next
        return head