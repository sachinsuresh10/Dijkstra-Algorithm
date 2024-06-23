# Dijkstra-Algorithm

# Shortest Route Finder using Dijkstra's Algorithm for Rail Networks

## Introduction

This repository contains the Python script implementing Dijkstra's algorithm for finding the shortest paths within a given rail network. The algorithm computes the shortest path from a designated starting station to all other stations in the network. This README provides an overview of the algorithm, its implementation, and instructions for running the script.

## Dijkstra's Algorithm Overview

Dijkstra's algorithm is used to find the shortest paths between nodes in a graph, particularly in scenarios where all edges have non-negative weights. In the context of a rail network:
- **Nodes**: Represent train stations.
- **Edges**: Represent direct routes between stations with travel times as weights.

### Key Terminologies
- **li→j**: Time taken to travel from station i to station j.
- **S**: Set of visited stations.
- **Y(j)**: Label representing the shortest time path from the starting station to station j.
- **P(j)**: Path label detailing the shortest path to station j.

### Algorithm Steps
1. **Initialization**:
   - Start with an empty set S containing only the starting station.
   - Set Y(s) = 0 (no time taken to reach the starting station).
   - Set P(s) = None (no path taken to reach the starting station).

2. **Iterative Process**:
   - Expand the set S by adding the station w that minimizes Y(i) + li→j for stations outside S, where (i, j) ∈ δ+(S).
   - Update Y(w) and P(w) accordingly.
   - Repeat until all stations are included in S.

### Example Execution
For instance, starting from Waterloo in a mini-network, iteratively find the shortest paths to other stations (Euston, Kings Cross, Paddington) as demonstrated in the worked example.

## Implementation Details

### Script Structure
- `dijkstra_route_finder.py`: Python script implementing Dijkstra's algorithm for finding shortest paths in a rail network.
- `rail_network_data.py`: Contains the representation of the rail network as a dictionary with stations and travel times.

### Running the Script
1. **Dependencies**:
   - Python 3.x
   - No additional libraries required beyond standard Python libraries.

2. **Execution**:
   - Run `dijkstra_route_finder.py`.
   - Input the starting station (e.g., Waterloo).
   - Output will display the shortest paths to all other stations in the network along with travel times.

### Testing
- The script has been tested on a smaller network for correctness and efficiency.
- Outputs for at least 4 different journeys within the network are validated as per project requirements.

## Code Documentation
- The script includes inline comments explaining each step of the algorithm and key function functionalities.
- Clear variable names and structured functions ensure ease of understanding and modification.

## Limitations and Future Improvements
- **Multiple Optimal Paths**: Currently, the script returns only one optimal path between stations. Future versions could provide multiple options.
- **Real-time Updates**: Incorporating real-time data for delays, maintenance, etc., would enhance accuracy.
- **Scalability**: Enhancing the algorithm's scalability for large-scale networks using advanced data structures and optimization techniques.

## Conclusion
This project demonstrates an effective implementation of Dijkstra's algorithm for finding shortest paths in a rail network. The algorithm's accuracy, efficiency, and potential enhancements are discussed, laying the groundwork for real-world application and further improvements.

For more details, refer to the full technical report and implementation in the repository.

---

This README provides an overview of the route finder project using Dijkstra's algorithm. For detailed technical insights and code implementation, refer to the repository files and documentation.
