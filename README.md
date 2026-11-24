# Polypharmacy-Side-Effect-Association-Network-Analysis
This project analyzes the Polypharmacy side-effect association network from the Stanford Network Analysis Project (SNAP). It models drug-drug interactions as a graph to identify and measure "connected components" for specific side effects.   
Polypharmacy (or concomitant drug usage) occurs when two drugs prescribed together elevate the risk of a specific side effect. In this graph model, nodes represent drugs (STITCH IDs) and edges represent the likelihood of developing a specific side effect when those two drugs are combined.

# Project Overview
The primary objective of this project is to answer a specific graph theory question: Of all the diseases whose graphs have exactly one connected component, which disease has the largest component?   
A connected component is a subset of a graph where:
+ There is a path from any node to any other node within the component.
+ There is no path between a node in one component and a node in another component.

# Implementation Details
+ Memory Efficiency: The script parses the compressed ```ChChSe-Decagon_polypharmacy.csv.gz``` file in a single read using a generator, avoiding the memory overhead of loading the entire global graph at once.
+ Zero External Dependencies: The connected components are discovered using a custom Breadth-First Search (BFS) algorithm rather than relying on heavy external graph libraries like ```networkx```.
+ Bonus Analytics: In addition to finding the largest single-component disease, the script evaluates every disease to output its total number of connected components and their average node size.

# Setup and Data 
To run this analysis, you need the SNAP polypharmacy dataset.   
1. Download [```ChChSe-Decagon_polypharmacy.csv.gz```](https://snap.stanford.edu/biodata/datasets/10017/files/ChChSe-Decagon_polypharmacy.csv.gz).
2. Do not decompress the file. The Python script reads the compressed archive directly using the built-in ```gzip``` module.

# Usage
The main script is ```Project_6.py```. Run it directly from your terminal:   
```
python Project_6.py
```
