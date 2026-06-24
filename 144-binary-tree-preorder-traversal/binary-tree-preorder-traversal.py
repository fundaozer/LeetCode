class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
            
        output = []
        
        def traverse(node):
            output.append(node.val)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
                
        traverse(root)
        return output

 

        