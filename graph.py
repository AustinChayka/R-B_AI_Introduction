import igraph as ig
import matplotlib.pyplot as plt

#graphing funtion to draw tree
def drawTree(vertices, edges) -> None:
    
    g = ig.Graph(directed=True)
    g.add_vertices(vertices)
    g.add_edges(edges)

    layout = g.layout("rt")
    layout.mirror(1)
    fig, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout=layout
    )
    plt.show()