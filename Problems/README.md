Notes

Recursion
- Uses a stack
- Internal stack is a "Call Stack"; data is "Stack Frames"

Tree
- Nodes, vertices: Abstraction of object
- Edges: Link between nodes
- Root: First/Parent node
- Internal node: Has at least one child
- Leaf node: No child nodes
- Ancestor: Nodes that are between the path from the root to current node
- Descendent: Nodes reachable from the current  node when moving down the tree
- Level: Number of ancestors from that node to the root
- Height: Number of edges on the longest path from that node to the leaf
- Depth: Number of edges on the path from the root to that node
- n-ary tree: Each node has no more than n children
- binary tree: n-ary tree with n = 2; every node has 0 - 2 children
- Full binary: Every node has 0 - 2 children
- Complete binary: All levels are completely filled except possibly the last level and all nodes in the last level are as far left as possible (usage in heap)
- Perfect binary: All internals nodes have 2 children and all leaf nodes have the same level. Used to estimate time complexity for combinatorial problems
- Balanced Binary: height difference of the left and right subtree of the node is not more than 1 (red-black trees, AVL)




Queue
Like a line; first in, first out
- Priority Queue: process according to priority; based on priority heap
- Queue<Double> queue = new LinkedList<>(); will display as entered
- Queue<Double> queue = new PriorityQueue<>(); will order
- Queue<Double> queue = new PriorityQueue<>(Collections.reverse)Order()); will order descending
- queue.offer(2.0) will add to queue
- while(!queue.isEmpty()) {
  System.out.println(queue.poll())}; will print queue
  