# -*- coding: utf-8 -*-
'''
First implementation of the dfs though this method will cause duplicates
'''
def dfs(matrix, start_node):
  n = len(matrix)  # Number of nodes
  visited_nodes = [False] * n  # Track visited nodes
  stack = []  # Stack for traversal
  path = []  # Stores traversal path

  stack.append(start_node)

  while stack:
    current_node = stack.pop()
    path.append(current_node)
    visited_nodes[current_node] = True

    for node in range(n):
      if not visited_nodes[node] and matrix[current_node][node] == 1:
        stack.append(node)  # Add unvisited neighbor to stack
  return path