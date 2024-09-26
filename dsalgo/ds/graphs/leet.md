## Adjancency matrix
- links b/w nodes can be represented using adjacency matrix
- represent all nodes along y -axis. do the same for x-axis
- now for a given node, if it has link with another node represent 1, rest represent with zeros. If its weighted link, use actual weights istead of ones
- for undirected links, adjacnecy matrix is always symmetric
- Space complexity: O(V^2), V - number of nodes, vertexes
- Time Complexity: Insert: O(V^2), Adding/Remove new link: O(1), removing node: O(V^2)

## Adjancency list
- insread os using nxn matrix we can instead use dict of str:list
- each key represnts a node name. value represents list of all node names connect to curr node
- Space complexity: O(V + E), V - number of nodes, e - link b/w two nodes
- Time Complexity: Adding new-node: O(1), Adding new link: O(1), Removing: O(E), removing node: O(V+E)