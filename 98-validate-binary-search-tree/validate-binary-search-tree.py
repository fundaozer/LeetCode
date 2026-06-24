class Solution(object):
    def isValidBST(self, root):
        def check(node,low,high):
            if not node:
                return True
            if not (low<node.val<high):
                return False

            left_valid=check(node.left,low,node.val)
            right_valid=check(node.right,node.val,high)

            return left_valid and right_valid
        return check(root,float("-inf"),float("inf"))

            
        