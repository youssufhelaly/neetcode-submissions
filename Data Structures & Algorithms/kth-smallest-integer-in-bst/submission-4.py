# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        f = root.val
        def traverse(root):
            if root is None:
                return
            nonlocal f
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)  
        traverse(root) 
        print(res)
        return res[k-1]