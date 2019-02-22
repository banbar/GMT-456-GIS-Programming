#Kruskal's Algorithm
#ref: https://www.youtube.com/watch?v=fAuF0EuZVCk
# Ref2: -requirement- Disjoint sets: https://www.youtube.com/watch?v=ID00PMy0-vE
import psycopg2
import io
from disjointSets import *
# io is needed to handle the Turkish characters and write them correctly into the txt file
# https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
import math

class polygons:
    def __init__(self, name, gid):
        self.name = name
        self.numNeighbours = 0
        self.neighbours = [[]]
        self.gid = gid
        # additional attribute: licencePlate code, abcRank

class postgres():
    def __init__(self, dbName, userName, pswd, host, port):
        try:
            self.conn = psycopg2.connect(database=dbName,
                            user=userName,
                            password=pswd,
                            host=host,
                            port=port)
            print("Connected to PostgreSQL Server")
        except:
            print("Postgres connection failed!")

class edgeTable:
    def __init__(self, table_edges, table_polygons, attr_name_polygon):
        self.table_edges = table_edges
        self.table_polygons = table_polygons
        self.attr_name_polygon = attr_name_polygon

def MST_Kruskal(inputFile):
    # The function accepts a txt file describing the connections
    # Reference: https://www.spoj.com/problems/BLINNET/
    # First line of the txt file: # of cities
    # Second line: First city name
    # Third line: How many connections does this city have?
    # n [number of cities <= 10 000]
    # NAME [city name]
    # p [number of neigbouring cities to the city NAME]
    # neigh cost 
    #      [neigh - the unique number of  city from the main list
    #      cost - the cost of building the blingors connection from NAME to neigh]

    f = io.open(inputFile, 'r', encoding="utf-8")

    numCities = int(f.readline().rstrip('\n'))

    # Create a 2D matrix stroing the weights between the nodes (cities)
    weights = [[-1 for x in range(numCities)] for y in range(numCities)]
    edgesList = [[0, [0, 0], 0]] # initialize the edges list
    # Initialize the list of vertices
    l_edges = [Node(ch) for ch in "-1"] # we will then pop this element
    edges = {}
    
    moreLines2Read = True
    cityID = 1
    edgeID = 1
    while(moreLines2Read):
        if(cityID == numCities+1):
            break
        # We are not interested in the city name.
        # Pass to the next line.
        f.readline()
        n1 = Node(cityID)
        l_edges.append(n1)
        # See how many edges does it have?
        numEdges = int(f.readline().rstrip('\n'))
        print(cityID, '-', numEdges)

        for i in range(numEdges):
            connection = f.readline().rstrip('\n').split(' ')
            weights[cityID-1][int(connection[0])-1] = int(connection[1])
            edgeString = str(cityID) + '-' + str(int(connection[0]))
            edges[edgeString] = int(connection[1])
            edgesList.append([edgeID, [cityID, int(connection[0])], int(connection[1])])
            edgeID += 1
        cityID += 1

    f.close()

    #print(weights) - OK
    # Sort the edgeList based on the weight values
    print("\n\nSorted List")

    edgesListSorted = sorted(edgesList, key=lambda l: l[2])
    edgesList = edgesListSorted
    del edgesListSorted

    # Remove the first edge which was used to initialize the list
    edgesList.pop(0)

    for i in range(len(edgesList)):
        print(edgesList[i], '\t', edgesList[i][1][1] )

    # Kruskal

    # Remove the first vertex ID - which was initialized to be -1
    l_edges.pop(0)

    # MakeSet for each of the vertex
    [MakeSet(node) for node in l_edges]

    # Resulting edge list - MST
    MST = [[]]
    cost = 0


    print(len(edgesList))

    for e in range(len(edgesList)):
        # Find the representative set of the edge
        root1 = Find(l_edges[edgesList[e][1][0]])
        root2 = Find(l_edges[edgesList[e][1][1]])
        # If both representative nodes are the same, then we form a cycle
        if(root1.data == root2.data):
            continue
        else:
            MST.append(edgesList[e][1])
            cost += edgesList[e][2]
            Union(root1, root2)

    print(MST)
    print(cost)

    f.close()

    return MST




def push2Postgres(MST, connSettings, tableName):
    try:
        conn = psycopg2.connect(database=connSettings[0],
                                user=connSettings[1],
                                password=connSettings[2],
                                host=connSettings[3],
                                port=connSettings[4])
        print("Connected to PostgreSQL Server")
    except:
        print("Postgres connection failed!")

    cur = conn.cursor()
    # Delete the table - just in case
    deleteTable = "DROP TABLE IF EXISTS public.{}".format(tableName)
    cur.execute(deleteTable)


    createTable = "CREATE TABLE {} ( origin integer, destination integer)".format(tableName)
    cur.execute(createTable)
    cur.close()

    # Insert the results
    cur = conn.cursor()
    for i in range(1, len(MST)):
        insertEdge = "INSERT INTO {} values({}, {})".format(tableName, MST[i][0], MST[i][1])
        cur.execute(insertEdge)

    print("Num of edges: ", len(MST))

    conn.commit()


def generateGraph(P, t, outFileName):
    cur = P.conn.cursor()
    query = "select gid, {} " \
            "from {}".format(t.attr_name_polygon, t.table_polygons)

    cur.execute(query)

    result = cur.fetchall()

    numCities = len(result)

    # create a list of city objects
    cities = []

    for i in range(numCities):
        city = polygons(result[i][1], result[i][0])
        cities.append(city)

    # Process the edges table and re-populate the cities table accordingly

    query = "select gid, origin, destination, weight, origin_gid, destination_gid  " \
            "from {}".format(t.table_edges)

    cur.execute(query)

    result = cur.fetchall()
    currentCityID = result[0][4]

    for i in range(len(result)):
        # print(result[i][2])
        # print(result[i][3])
        cities[result[i][4] - 1].neighbours.append([result[i][5], result[i][3]])
        cities[result[i][4] - 1].numNeighbours += 1

    # Cities is generated correctly!
    # Need to prepare the txt file correctly


    f = io.open(outFileName, "w", encoding="utf-8")
    f.write(str(numCities) + "\n")

    for i in range(numCities):
        # Some polygon names could have '\n' inherently
        # Those '\n's must be removed

        print(cities[i].name)
        #f.write(cities[i].name.rstrip('\n') + "\n")
        # Writing the polygon names, somehow, lead to a ValueError:
        # ValueError: invalid literal for int() with base 10: ''
        # Therefore, instead of the polygon name, we write its geometry ID starting from 1
        f.write(str(i+1) + "\n")
        f.write(str(cities[i].numNeighbours) + "\n")
        for j in range(1, cities[i].numNeighbours + 1):
            print(cities[i].neighbours[j][0])
            print(cities[i].neighbours[j][1])

            # We need to accommodate both geographical and projected coordinates
            if (cities[i].neighbours[j][1] < 1):
                f.write(str(cities[i].neighbours[j][0]) + " " + str(
                    math.floor(cities[i].neighbours[j][1] * 1000000)) + "\n")
            else:  # we are in the projected coordinates - the values are quite big
                f.write(str(cities[i].neighbours[j][0]) + " " + str(math.floor(cities[i].neighbours[j][1])) + "\n")

    f.close()



# Connection settings
dbName = "tr_mst_ilce"
userName = "postgres"
pswd = "12345Aa"
host = "127.0.0.1" #localhost
port = "5432"
connPostgres= [dbName, userName, pswd, host, port]


P = postgres(*connPostgres)

nameEdgesTable = "edges"
namePolygonsTable = "p_ilceler"
nameAttrNamePolygon = "name_2"

#table = edgeTable(table_edges = 'edges', table_polygons = 'ilceler', attr_name_polygon = "name_2")
table = edgeTable(table_edges = nameEdgesTable, table_polygons = namePolygonsTable, attr_name_polygon = nameAttrNamePolygon)

# Generate the graph -> the output is in the SPOJ format
# Reference: https://www.spoj.com/problems/BLINNET/

outFile = "tr_ilceler.txt"
generateGraph(P, table, outFile)

# Symmetric structure would need to be handled!
# Use disjoint sets to determine whih edge to include in the MST
# The lower edgeID represents the set



MST = MST_Kruskal(outFile)


outTablePostgres = "results"
push2Postgres(MST, connPostgres, outTablePostgres)

# Issue

