# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def getDepthWithParent(parent, target):
            """
                this function get the depth of the target and each time pass the parent with it
                parameters:
                    parent: the parent of target node
                    target: the target want to get depth of if
                returns (parent, depth)
            """
            # if no elements in the parent, return nothing
            if not parent or parent.val == target or not parent.left and not parent.right:
                return [None, 0]
            # check if the target is in any child of the parent
            if parent.left and parent.left.val == target or parent.right and parent.right.val == target:
                return [parent, 1]

            # search in left
            search_in_left = getDepthWithParent(parent.left, target)

            if search_in_left[0]:
                search_in_left[1] += 1
                return search_in_left

            # search in right
            search_in_right = getDepthWithParent(parent.right, target)
            search_in_right[1] += 1
            return search_in_right

        x_analysis = getDepthWithParent(root, x)
        y_analysis = getDepthWithParent(root, y)

        return True if x_analysis[1] == y_analysis[1] and x_analysis[0] is not y_analysis[0] else False
