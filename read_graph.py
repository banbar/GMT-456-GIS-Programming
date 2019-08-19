
def read_graph(input_graph):
    # Format of the input txt file:
    # [number of nodes of the graph]
    # [name of the node]
    # [number of neighbours of the node]
    # [neighbour name] [cost of the edge]

    f = open(input_graph, 'r')
    numNodes = int(f.readline().rstrip('\n'))

    # Edge IDs start from 1
    e_id = 1
    nodes = {}
    edges = [[]] #each edge consists of an ID, the nodes of the edge and cost
                 # E.g. edges[3] = [3, ['A', 'C'], 12]

    # iterate for all of the nodes
    for i in range(numNodes):
        # Get the name of the node
        name_node = f.readline().rstrip('\n')
        num_neighbors = int(f.readline().rstrip('\n'))

        # In order to handle islands -i.e. a node with no neighbor
        if(num_neighbors == 0):
            continue

        # Obtain the first neighbor
        neighbor = f.readline().rstrip('\n').split(' ')
        # Cost of an edge should be recorded as an integer
        neighbor = [neighbor[0], float(neighbor[1])]

        # Have we recorded the current node? - check whether it exists in the nodes dictionary
        if name_node in nodes.keys():
            # Read the neighbour and record it
            nodes[name_node].append(neighbor)

        else:
            # Create a new dictionary item
            # Read its first neighbour and add it
            nodes[name_node] = [neighbor]

        # Generate an edge - to accommodate real values, we convert the string cost into a float
        edges.append([e_id, [name_node, neighbor[0]], float(neighbor[1])])
        e_id += 1

        # Add the remaining neighbors
        for j in range(num_neighbors-1):
            neighbor = f.readline().rstrip('\n').split(' ')
            # Cost of an edge should be recorded as a float
            neighbor = [neighbor[0], float(neighbor[1])]
            nodes[name_node].append(neighbor)

            # Generate an edge
            edges.append([e_id, [name_node, neighbor[0]], float(neighbor[1])])
            e_id += 1


    # Remove the first empty edge
    edges.pop(0)

    f.close()

    return nodes, edges
