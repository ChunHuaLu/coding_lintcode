from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        queue = deque([root])
        lv_order = []
        lv_order.append([root.val])
        while queue:
            tmp = []
            for _ in range(0,len(queue)):
                node = queue.popleft()
                if node.left:
                    l_child = node.left
                    queue.append(l_child)
                    tmp.append(l_child.val)
                if node.right:
                    r_child = node.right
                    queue.append(r_child)
                    tmp.append(r_child.val)
            if len(tmp) > 0:
                lv_order.append(tmp)
        return lv_order