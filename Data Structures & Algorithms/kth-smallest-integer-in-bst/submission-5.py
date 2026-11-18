# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        count = k
        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            res.append(root.val)
            if len(res) == k:
                return
            traverse(root.right)  
        traverse(root) 

        return res[k-1]