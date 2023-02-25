# Problem Link: https://www.hackerrank.com/challenges/30-binary-trees

# My Solution:

def levelOrder(self, root):
  if not root:
    return
  
  queue = [root]    
  while queue:
    node = queue.pop(0)
    print(node.data, end=' ')
    
    if node.left:
      queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
