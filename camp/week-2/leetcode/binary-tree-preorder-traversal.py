# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []

        def preorder(node,stack):
            if node == None:
                return
            stack.append(node.val)
            preorder(node.left,stack)
            preorder(node.right,stack) 

            return stack

        return preorder(root,stack)


