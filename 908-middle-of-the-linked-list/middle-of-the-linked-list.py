
class Solution(object):
    def middleNode(self, head):
        middle=head
        end=head
        while end and end.next:
            middle=middle.next
            end=end.next.next
        return middle
        