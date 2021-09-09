
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

- 中序遍历递归

```python
def 中序遍历递归(root:TreeNode):
    if not root: return
    self.seq = []
    def in_order(node):
        if not node: return
        in_order(node.left)
        self.seq.append(node.val)
        in_order(node.right)
    in_order(root)
    return self.seq[-k]
```

- 中序遍历非递归

```python
def 中序遍历非递归(root:TreeNode):
    if not root: return
    stack = []
    seq = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        seq.append(root.val)
        root = root.right           
    return seq[-k]
```

- 逆中序遍历递归

```python
def 逆中序遍历递归(root:TreeNode):
    if not root: return
    self.k = k
    def inverse_in_oder(node):
        if not node: return
        l = inverse_in_oder(node.right)
        self.k -= 1
        if self.k == 0: 
            return node.val
        r = inverse_in_oder(node.left)
        return l or r
    return inverse_in_oder(root)
```

- 逆中序遍历非递归

```python
def 逆中序遍历非递归(root:TreeNode)
    stack = []
    if not root: return
    while stack or root:
        while root:
            stack.append(root)
            root = root.right
        node = stack.pop()
        k -= 1
        if k == 0: return node.val
        root = node.left
```