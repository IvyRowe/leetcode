# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[root.val]]
        n=1
        self.helpzigzag(root, result, n)
        
        result = [ele for ele in result if ele]
        
        for ele in result[1::2]:
            ele.reverse()
        
        return result
        
    def helpzigzag(self, root, result, n):
        if not root:
            return
        if len(result) <= n:
            result.append([])
        if root.left:
            result[n].append(root.left.val)
        if root.right:
            result[n].append(root.right.val)
        
        self.helpzigzag(root.left, result, n+1)
        self.helpzigzag(root.right, result, n+1)
