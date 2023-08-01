# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        out=[(root,root.val)]
        while out:
            node,val=out.pop()
            if not node.left and not node.right and val==targetSum:
                return True
            if node.left:
                out.append((node.left, val + node.left.val))
            if node.right:
                out.append((node.right, val + node.right.val))
        
        return False
            