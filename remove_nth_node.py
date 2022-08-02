from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def count_itens(head: Optional[ListNode]):
            total = 0
            while head:
                total += 1
                head = head.next

            return total

        def search_node(pos: int, head: ListNode, before: ListNode = None) -> ListNode:
            next = head
            while pos <= (total - n) + 1:
                if pos == total - n + 1:
                    if before:
                        before.next = next.next
                    else:
                        return next.next
                    break
                else:
                    pos += 1
                    before = next
                    next = next.next

            return head

        if head.next is None:
            return head.next

        total = count_itens(head)
        return search_node(1, head)

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


if __name__ == '__main__':
    head = make_list([1, 2])
    n = 2

    solution = Solution()
    val = solution.removeNthFromEnd(head, n)
    print(val)