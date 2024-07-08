import networkx as nx
import json

# Create a simple graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)])

# Convert the graph to a JSON format
data = nx.node_link_data(G)
json_data = json.dumps(data)

# Save JSON data to a file (optional, for reference)
with open('graph.json', 'w') as f:
    f.write(json_data)
