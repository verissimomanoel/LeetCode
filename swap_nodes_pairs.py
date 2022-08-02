from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        node = head
        while node:
            if count % 2 != 0 and node.next:
                aux = node.val
                node.val = node.next.val
                node.next.val = aux

            node = node.next
            count += 1

        return head

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head

if __name__ == '__main__':
    head = make_list([1, 2, 3, 4])

    solution = Solution()
    val = solution.swapPairs(head)
    print(val)