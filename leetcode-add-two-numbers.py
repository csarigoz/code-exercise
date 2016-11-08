# Problem URL: https://leetcode.com/problems/add-two-numbers/
# Couldn't make it to return a linked list, just returned a list instead.
# LeetCode accepted it anyway :)
# Here is a solution I've found on the web afterwards: http://jelices.blogspot.com.tr/2014/05/leetcode-python-add-two-numbers.html
#

# Definition for singly-linked list.
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
        n1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            n1 = str(l1.val) + n1

        n2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            n2 = str(l2.val) + n2

        nSum = str(int(n1) + int(n2))
        lSum = []

        for i in range(-1, -len(nSum) - 1, -1):
            lSum.append(int(nSum[i]))

        return lSum