# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = []
        di = defaultdict(list)
        maxim = 0
        def traverse (root,level,value):
            nonlocal di
            if not root:
                return 
            di[level].append(value)
            traverse(root.left,level + 1,2 * value + 1)
            traverse(root.right, level +1,2 * value + 2)

        traverse(root,1,0)
        for num in di.values():
            maxim = max (maxim,num[-1] - num[0] + 1)
        return maxim