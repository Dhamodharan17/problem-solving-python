class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []
        def util(root):
            # go till end of the each tree end
            if root is None:
                return
              
            util(root.left)
            output.append(root.val)
            util(root.right)

        util(root)
        return output
