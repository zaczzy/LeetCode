# Definition for singly-linked list.
from math import pow


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_string(self):
        num_str = ""
        cursor = self
        while cursor is not None:
            num_str = str(cursor.val) + num_str
            cursor = cursor.next
        return num_str

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        order_magnitude = 0
        while l1 is not None:
            sum = sum + int(l1.val * pow(10, order_magnitude))
            l1 = l1.next
            order_magnitude += 1
        order_magnitude = 0
        while l2 is not None:
            sum = sum + int(l2.val * pow(10, order_magnitude))
            l2 = l2.next
            order_magnitude += 1
        head, curr = None, None
        # Use your own length counter and not the default log(n, 10) one!
        length = 1
        copy = sum
        while copy // 10 != 0:
            copy = copy // 10
            length += 1

        for i in range(length):
            new_node = ListNode(int(sum // pow(10, i)) % 10)
            if curr is not None:
                curr.next = new_node
                curr = curr.next
            else:
                head = curr = new_node
        return head

if __name__ == "__main__":
    l1 = ListNode(5)
    print(l1.to_string())
    l2 = ListNode(5)
    print(l2.to_string())
    sum = Solution().addTwoNumbers(l1, l2)
    print(sum.to_string())
