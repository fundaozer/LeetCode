class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []

        output=[]
        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            output.append(node.val)
            traverse(node.right)
        traverse(root)
        return output

        