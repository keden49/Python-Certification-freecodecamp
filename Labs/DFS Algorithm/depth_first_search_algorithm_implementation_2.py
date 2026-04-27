
'''
This implementation avoids duplicate node values
'''
def dfs(matrix, start_node):
  n = len(matrix)  # Number of nodes
  visited_nodes = [False] * n  # Track visited nodes
  stack = []  # Stack for traversal
  stack.append(start_node)
  visited_nodes[start_node] = True

  path = []  # Stores traversal path



  while stack:
    current_node = stack.pop()
    path.append(current_node)
    #visited_nodes[current_node] = True

    for node in range(n):
      if not visited_nodes[node] and matrix[current_node][node] == 1:
        '''To avoid duplicates/ nodes being processed twice
        a node should be marked as visited at the exact moment its being added to the stack
        '''
        stack.append(node)  # Add unvisited neighbor to stack
        visited_nodes[node] = True

  return path

