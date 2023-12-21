# my_module/graph_operations.py
import networkx as nx
import matplotlib.pyplot as plt

def create_and_visualize_graph():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

def check_eulerian_cycle(graph):
    if nx.is_eulerian(graph):
        print("The graph has an Eulerian cycle.")
    else:
        print("The graph does not have an Eulerian cycle.")
