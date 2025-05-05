
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
assigned_colors = {}

def is_safe(node, color):
    for neighbor in graph[node]:
        if neighbor in assigned_colors and assigned_colors[neighbor] == color:
            return False
    return True

def color_graph(nodes, index):
    if index == len(nodes):
        return True
    node = nodes[index]
    for color in colors:
        if is_safe(node, color):
            assigned_colors[node] = color
            if color_graph(nodes, index + 1):
                return True
            del assigned_colors[node] 
    return False

nodes = list(graph.keys())
if color_graph(nodes, 0):
    print("Color assignment:")
    for node in assigned_colors:
        print(f"{node} ---> {assigned_colors[node]}")
else:
    print("No valid coloring found.")
