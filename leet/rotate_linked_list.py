#Given the head of a linked list, rotate the list to the right by k places.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]
#Example 2:
#
#
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 500].
#-100 <= Node.val <= 100
#0 <= k <= 2 * 109
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #print(head)
        #head2 = copy.deepcopy(head)
        if not head or k ==0:
            return head
        elif not head.next:
            return head
        

        head2 = head
        length = 1        
        while head.next:
            head = head.next
            length += 1
        if k ==length or (k - int(k/length)*length) ==0:
            return head2
        head = head.next
        #tail = head
        #print(head)
        #print(length)
        to_be_rev = length - (k - int(k/length)*length)
        #print(head2)
        h = 1
        while to_be_rev:
            if h == 1:
                tail = ListNode(head2.val)
                tailh = tail
                h += 1
            else:
                tail.next = ListNode(head2.val)
                #print(tail)
                tail = tail.next
            head2 = head2.next
            to_be_rev -= 1
        #print(tailh)
        #print(head2)
        headf = head2
        while head2.next:
            head2 = head2.next
        head2.next = tailh
        #print(headf)
        return headf
