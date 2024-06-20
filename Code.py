#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculate the shortest path for any starting point, and the output result should include the starting point, destination point, shortest path, and time


# In[6]:


import heapq

def dijkstra(graph, start):
    '''
    This function calculates the shortest path to every station in the graph from the start station
    
    Parameters
    ----------
    graph: dictionary
        Information of the network
    start: str
        The start station

    Returns
    -------
    distances: dictionary
        The shortest time from the starting node to each node
    previous_nodes: dictionary
        Previous node on the shortest path to each node
    '''
    # Initialization
    S = set()  # The set of nodes that have been visited
    distances = {node: float('infinity') for node in graph}  # Record the shortest time from the starting node to each node, default to infinity
    previous_nodes = {node: None for node in graph}  # Record the previous node on the shortest path to each node, defaulting to None
    distances[start] = 0  # The time from the starting node to itself is 0
    priority_queue = [(0, start)]  # Using heap to implement priority queues, storage nodes and corresponding shortest times

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Retrieve the node with the shortest current time from the heap

        if current_node not in S:
            S.add(current_node)  # Mark the current node as visited

            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight  # Calculate the time from the current node to neighboring nodes

                if distance < distances[neighbor]:
                    distances[neighbor] = distance  # Update the shortest time to reach neighboring nodes
                    previous_nodes[neighbor] = current_node  # Record the previous node of neighboring nodes on the shortest path
                    heapq.heappush(priority_queue, (distance, neighbor))  # Add neighboring nodes and their new shortest time to the priority queue

    return distances, previous_nodes


def get_shortest_path(graph, start, end):
    '''
    This function calculates the shortest path from the start station to the end station in the graph
    
    Parameters
    ----------
    graph: dictionary
        Information of the network
    start, end: str
        The start and end station

    Returns
    -------
    path: list
        The shortest path from the start station to the end station
    distances[end]: float
        The time from the start station to the end through the shortest path
    '''
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current_node = end

    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)  # Insert the current node into the beginning of the path
        current_node = previous_nodes[current_node]  # Backtrack to the previous node

    path.insert(0, start)  # Insert the starting node into the beginning of the path
    return path, distances[end]


def get_shortest_path_users(graph, start, end):
    '''
    This function outputs the shortest path and time for users from the start station to the end station in the graph
    
    Parameters
    ----------
    graph: dictionary
        Travelling time between stations in the network,
        for example：
            graph = {
                'W': {'E': 8},
                'E': {'W': 8, 'KC': 4, 'P': 6},
                'KC': {'E': 4, 'P': 1},
                'P': {'E': 6, 'KC': 1}
            }
    start, end: str
        The start and end station

    Returns
    -------
    Print the shortest path and time from the start station to the end station in the graph
    
    '''
    # Run Dijkstra algorithm
    shortest_path, shortest_time = get_shortest_path(graph, start_station, destination_station)

    # Print the results
    print(f"Starting station: {start_station}")
    print(f"Destination station: {destination_station}")
    print(f"Time: {shortest_time} minutes")
    print(f"Route: {' → '.join(shortest_path)}")


# In[7]:


# Test Networl 1
graph = {
    'W': {'E': 8},
    'E': {'W': 8, 'KC': 4, 'P': 6},
    'KC': {'E': 4, 'P': 1},
    'P': {'E': 6, 'KC': 1}
}

# Set the starting and destination stations
start_station = 'E'
destination_station = 'P'

# Output results
get_shortest_path_users(graph, start_station, destination_station)


# In[8]:


# Definition of the network
graph = {
    'Paddington': {'Baker Street': 6, 'Notting Hill Gate': 4},
    'Baker Street': {'Paddington': 6, 'Bond Street': 2, 'Kings Cross': 7, 'Oxford Circus': 4},
    'Notting Hill Gate': {'Paddington': 4, 'Bond Street': 7,'South Kensington': 7},
    'Bond Street': {'Baker Street': 2, 'Notting Hill Gate': 7,'Oxford Circus': 1, 'Green Park': 2},
    'Kings Cross': {'Baker Street': 7, 'Warren Street': 3, 'Holbom': 4, 'Moorgate': 6, 'Old Street': 6},
    'Oxford Circus': {'Baker Street': 4, 'Bond Street': 1, 'Green Park': 2, 'Piccadilly Circus': 2, 
                      'Tottenham Court Road': 2, 'Warren Street': 2},
    'South Kensington': {'Notting Hill Gate': 7, 'Green Park': 7, 'Victoria': 4},
    'Green Park': {'Bond Street': 2, 'South Kensington': 7, 'Victoria': 2, 'Westminster': 3, 'Piccadilly Circus': 1, 'Oxford Circus': 2},
    'Warren Street': {'Kings Cross': 3, 'Oxford Circus': 2, 'Tottenham Court Road': 3},
    'Holbom': {'Kings Cross': 4, 'Tottenham Court Road': 2, 'Leicester Square': 2, 'Bank': 5},
    'Moorgate': {'Kings Cross': 6, 'Bank': 3, 'Liverpool Street': 2, 'Old Street': 1},
    'Old Street': {'Kings Cross': 6, 'Moorgate': 1},
    'Piccadilly Circus': {'Oxford Circus': 2, 'Green Park': 1, 'Charing Cross': 2, 'Leicester Square': 2},
    'Tottenham Court Road': {'Oxford Circus': 2, 'Leicester Square': 1, 'Holbom': 2, 'Warren Street': 3},
    'Victoria': {'South Kensington': 4, 'Green Park': 2, 'Westminster': 4},
    'Westminster': {'Green Park': 3, 'Victoria': 4, 'Waterloo': 2, 'Embankment': 2},
    'Leicester Square': {'Holbom': 2, 'Tottenham Court Road': 1, 'Piccadilly Circus': 2, 'Charing Cross': 2},
    'Bank': {'Holbom': 5, 'Blackfriars': 4, 'London Bridge': 2, 'Tower Hill': 2, 'Liverpool Street': 2, 'Moorgate':3},
    'Liverpool Street': {'Moorgate': 2, 'Bank': 2, 'Tower Hill': 6, 'Aldgate East': 4},
    'Charing Cross': {'Leicester Square': 2, 'Piccadilly Circus': 2, 'Embankment': 1},
    'Embankment': {'Westminster': 2, 'Charing Cross': 1, 'Waterloo': 2, 'Blackfriars': 4},
    'London Bridge': {'Bank': 2, 'Waterloo': 3, 'Elephant and Castle': 3},
    'Tower Hill': {'Bank': 2, 'Liverpool Street': 6, 'Aldgate East': 2},
    'Aldgate East': {'Liverpool Street': 4, 'Tower Hill': 2},
    'Waterloo': {'Embankment': 2, 'Westminster': 2, 'Elephant and Castle': 4, 'London Bridge': 3},
    'Blackfriars': {'Embankment': 4, 'Bank': 4},
    'Elephant and Castle': {'Waterloo': 4, 'London Bridge': 3}
}

# Test 1
# Set the starting and destination stations
start_station = 'Paddington'
destination_station = 'London Bridge'

# Output results
get_shortest_path_users(graph, start_station, destination_station)


# In[9]:


# Test 2
# Set the starting and destination stations
start_station = 'Embankment'
destination_station = 'Tottenham Court Road'

# Run Dijkstra algorithm
shortest_path, shortest_time = get_shortest_path(graph, start_station, destination_station)

# Output results
get_shortest_path_users(graph, start_station, destination_station)


# In[10]:


# Test 3
# Set the starting and destination stations
start_station = 'Notting Hill Gate'
destination_station = 'Waterloo'

# Run Dijkstra algorithm
shortest_path, shortest_time = get_shortest_path(graph, start_station, destination_station)

# Output results
get_shortest_path_users(graph, start_station, destination_station)


# In[12]:


# Postscript: test for station to station
stations = ['Paddington', 'Baker Street','Notting Hill Gate','Bond Street','Kings Cross','Oxford Circus','South Kensington','Green Park',
    'Warren Street','Holbom','Moorgate','Old Street','Piccadilly Circus','Tottenham Court Road','Victoria','Westminster','Leicester Square','Bank',
    'Liverpool Street','Charing Cross','Embankment','London Bridge','Tower Hill','Aldgate East','Waterloo','Blackfriars','Elephant and Castle']

for start_station in stations:
    for destination_station in stations:
    # Run Dijkstra algorithm
        shortest_path, shortest_time = get_shortest_path(graph, start_station, destination_station)
        print(f"Time: {shortest_time} minutes")
        print(f"Route: {' → '.join(shortest_path)}")
    


# In[ ]:




