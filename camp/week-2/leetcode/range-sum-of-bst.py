# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root :
            return self.sums
        self.rangeSumBST(root.left,low,high)
        if(root.val>=low and root.val <= high):
            self.sums += root.val
        self.rangeSumBST(root.right,low,high)
        return self.sums
