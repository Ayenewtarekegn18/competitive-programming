# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        i = 0 
        ans = TreeNode()
      
        def traverse(root,val):
            nonlocal ans,i
            if root == None or i != 0:
                return 
            if root.val == val:
                i -= 1
                ans = root
            traverse(root.left,val)
            traverse(root.right,val)
        traverse(root,val)
        return ans if ans.val != 0 else None