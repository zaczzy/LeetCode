# Definition for singly-linked list.
from math import log, pow
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    def make_list_node(self, num):
        highest_term = int(log(num) / log(10))
        prev = ListNode(int(num / pow(10, highest_term)))
        for i in range(1, highest_term):
            current = ListNode(int(num / pow(10, highest_term - i)))
            current.next = prev
            prev = current
        return current

    def test_list_node(self, l):
        print('The 1st value is' + l.val)
        i = 2
        while(l.next is not None):
            l = l.next
            print('The '+ i + 'th value is' + l.val)
            i += 1