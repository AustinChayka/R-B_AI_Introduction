from tree import TreeNode
import igraph as ig
import matplotlib.pyplot as plt

def drawTree(root: TreeNode):
    
    g = ig.Graph(directed=True)
    g.add_vertices(root.size())
    g.add_edges(root.get_edges())

    layout = g.layout("rt")
    layout.mirror(1)
    fig, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout=layout
    )
    plt.show()