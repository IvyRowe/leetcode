class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, tmp, stack, flag = [], [], [root], False
        
        while stack:
            for i in range(len(stack)):
                cur = stack.pop(0)
                tmp.append(cur.val)
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
            if flag:
                tmp.reverse()
            res.append(tmp)
            tmp = []
            flag = not flag
        
        return res
