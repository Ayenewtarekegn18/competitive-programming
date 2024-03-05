# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        di = defaultdict(list)
        def traverse (root,level):
            nonlocal di
            if not root:
                return 
            di[level].append(root.val)
            traverse(root.left,level + 1)
            traverse(root.right, level +1)

        traverse(root,1)

        for key,val in di.items():
            if key % 2 == 0:
                ans.append(val[::-1])
            else:
                ans.append(val)
        return ans