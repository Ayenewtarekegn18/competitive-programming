# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def traverse(root):
            nonlocal stack
            if not root:
                return
            traverse(root.left)
            stack.append(root.val)
            traverse(root.right)
        traverse(root)
        for i in range(len(stack) - 1):
            if stack[i] >= stack[i+1]:
                return False
        return True