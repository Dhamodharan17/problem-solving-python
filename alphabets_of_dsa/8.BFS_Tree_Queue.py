class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []
        if not root:
            return output

        queue = deque([root])

        while queue:

            size = len(queue)
            res = []
            #level wise
            for i in range(size):
                current = queue.popleft()
                res.append(current.val)
                if current.left:queue.append(current.left)
                if current.right:queue.append(current.right)

            output.append(res)

        return output
