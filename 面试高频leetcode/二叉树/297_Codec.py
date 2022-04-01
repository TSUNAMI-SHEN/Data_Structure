# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.split_s = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#,'
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == None:
            return None
        if data == '#':
            return None
        self.split_s = data.split(',')
        return self.construct()
        
    def construct(self):
        if self.split_s[0] == '#':
            self.split_s = self.split_s[1:]
            return None
        node = TreeNode(int(self.split_s[0]))
        node.left = None
        node.right = None

        self.split_s = self.split_s[1:]
        node.left = self.construct()
        node.right = self.construct()

        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
