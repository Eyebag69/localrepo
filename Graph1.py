# A tree where each node has 3 branches
ternary_tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I', 'J'],
    'D': ['K', 'L', 'M'],
    'E': [], 'F': [], 'G': [], 'H': [],
    'I': [], 'J': [], 'K': [], 'L': [], 'M': []
}

def BFS(ternary_tree,Node):
  visited=[]
  queue=[]
  visited.append(Node)
  queue.append(Node)
  while queue:
    m = queue.pop(0)
    print(m,end= " ")
    for n in ternary_tree[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)
BFS(ternary_tree, "A")
