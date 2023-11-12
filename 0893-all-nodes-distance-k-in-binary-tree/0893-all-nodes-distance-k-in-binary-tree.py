# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        seen = set()
        dic = collections.defaultdict()

        def populateParent(root, parent):
            if not root:
                return
            dic[root] = parent
            populateParent(root.left, root)
            populateParent(root.right, root)

        def bfs(root):
            q = deque()
            q.append([root, 0])
            while q:
                n = len(q)
                for i in range (n):
                    node, d = q.popleft()

                    if not node or node in seen:
                        continue
                    
                    seen.add(node)

                    if d == k:
                        res.append(node.val)

                    if node.left:
                        q.append([node.left, d + 1])
                    if node.right:
                        q.append([node.right, d + 1])
                    if node in dic:
                        q.append([dic[node], d + 1])

        populateParent(root, None)
        bfs(target)
        return res

        