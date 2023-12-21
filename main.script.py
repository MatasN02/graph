# main_script.py
from my_module.graph_operations import create_and_visualize_graph, check_eulerian_cycle

if __name__ == "__main__":
    # Ensure that the 'my_module' directory is in sys.path
    import sys
    sys.path.append("path/to/my_project")

    # Create and visualize the graph
    graph = create_and_visualize_graph()

    # Check for Eulerian cycle
    check_eulerian_cycle(graph)
