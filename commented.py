#Student name: Sara Filekovic
#Project: Shortest path between 2 cities

import networkx as netx #Python package with functions for creation and analysis of network graphs
import csv #Python module for data in .csv format

#opening and reading the file with city nodes
#encoding system is specified since we are working with text files
with open('cityName.csv', 'r', encoding='utf-8') as nodesFile:
    readInNodes = csv.reader(nodesFile)
    #creating a list of nodes, excluding the file's header (cityID and name)
    nodes = [node for node in readInNodes][1:]
#creating a list of city IDs
cityIDs = [cityNode[0] for cityNode in nodes]

#opening and reading the file with edges
with open('FromTo.csv', 'r', encoding='utf-8') as edgesFile:
    readInEdges = csv.reader(edgesFile)
    #creating a list of edges, excluding the file's header (fromNode, toNode)
    edges = [edge for edge in readInEdges][1:]

#test 1: testing whether we have a correct number of nodes and edges, and whether they print properly
print("Number of nodes:", len(cityIDs))
print("Number of edges:", len(edges))
print("City IDs:", cityIDs)
print("Edges:", edges)

#creating a graph object and filling it with nodes(cityIDs) and edges(fromNode/cityID and toNode/cityID)
graphPlot = netx.Graph()
graphPlot.add_nodes_from(cityIDs)
graphPlot.add_edges_from(edges)

#test 2: printing the fundamental information about the graph
print(netx.info(graphPlot))

#city names - attribute of city nodes (NetworkX functions used below require us to use a Python dictionary here)
cityNames = {}
#traversing the list of nodes and setting each city name as an attribute of its corresponding city ID
for cityNode in nodes:
    cityNames[cityNode[0]] = cityNode[1]
netx.set_node_attributes(graphPlot, cityNames, 'City Name')

#test 3: printing city IDs and their corresponding names
for cityNode in graphPlot.nodes():
    print(cityNode, graphPlot.nodes[cityNode]['City Name'])

#taking the names of two cities (source and destination) as an input
sourceCity = input("Enter source:")
destinationCity = input("Enter destination:")
#checking whether the graph contains the entered cities and accessing their corresponding IDs
for cityNode1 in graphPlot.nodes():
    if graphPlot.nodes[cityNode1]['City Name'] == sourceCity:
        sourceCity = cityNode1
for cityNode2 in graphPlot.nodes():
    if graphPlot.nodes[cityNode2]['City Name'] == destinationCity:
        destinationCity = cityNode2

#function that implements the shortest path algorithm on our graph using breadth-first search, since the graph is
#unweighted and undirected
def get_shortest_path(graph, source, destination):
    visitedCities = [] #keeping a list of visited cities, in order to evade cycles
    pathList = [[source]] #list of cities we are currently visiting, starting from the source

    #traversing the path list while it is not empty
    while pathList:
        path = pathList.pop(0) #popping the first city/set of cities added to the list and placing them on the path
        currentCity = path[-1] #accessing the last city on that path, which will now be our current city (in the first
        #traversal, this is still the source city)

        if currentCity not in visitedCities:
            neighborCities = graph[currentCity] #storing all the adjacent/neighboring cities of the current city

            for eachCity in neighborCities:
                shortest_path = list(path) #creating a new list from the initial path, that will be our shortest path
                shortest_path.append(eachCity) #placing the neighboring cities on that path
                pathList.append(shortest_path) #adding the shortest path to the path list

                if eachCity == destination: #once we reach the destination, shortest path is printed
                    print("Shortest path:", shortest_path)
                    print("Distance:", netx.shortest_path_length(graph, source, destination))
                    return
            visitedCities.append(currentCity) #adding the current city to the list of visited cities
    print("No path exists between the entered cities.") #case when there is no path between the entered cities
    return

#calling the function with the shortest path algorithm implementation
#we pass in as parameters: the created graph, the source city and the destination city that the user enters
get_shortest_path(graphPlot, sourceCity, destinationCity)