import graph
from tree import TreeNode as tn
import time

root = tn(children=[tn(children=[tn(), tn(children=[tn(), tn()])]), tn(children=[tn(children=[tn(), tn()])])])

graph.drawTree(root)