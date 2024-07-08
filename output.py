import networkx as nx
import json

# Create a simple graph with additional attributes
G = nx.DiGraph()
G.add_nodes_from([
    (1, {"color": "red", "shape": "circle"}),
    (2, {"color": "blue", "shape": "rect"}),
    (3, {"color": "green", "shape": "circle"}),
    (4, {"color": "orange", "shape": "rect"}),
    (5, {"color": "purple", "shape": "circle"}),
    (6, {"color": "yellow", "shape": "rect"})
])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)])

# Convert the graph to a JSON format
data = nx.node_link_data(G)
json_data = json.dumps(data, indent=4)

# Save JSON data to a file
with open('graph.json', 'w') as f:
    f.write(json_data)

# Print JSON data
print(json_data)
