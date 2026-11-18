# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k
        def traverse(root):
            nonlocal res, count
            if root is None:
                return
            if count == 0:
                return
            traverse(root.left)
            count -= 1
            if count == 0:
                res = root.val
                return
            traverse(root.right)  
        traverse(root) 
        print(res)
        return res