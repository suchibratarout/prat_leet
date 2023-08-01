# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        out=[[root,1]]
        res=0
        while out:
            node,depth=out.pop()
            if node:
                res=max(res,depth)
                out.append([node.left,depth+1])
                out.append([node.right,depth+1])
        return res
