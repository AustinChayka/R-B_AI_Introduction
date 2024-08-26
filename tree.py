class TreeNode(object):

    def __init__(self, data=None, name='root', children=None):
        self.data = data
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    
    def __repr__(self) -> str:
        return self.name
    
    def add_child(self, child):
        assert isinstance(child, TreeNode)
        self.children.append(child)

    def size(self) -> int:
        if self.children == None:
            return 1
        return 1 + sum([child.size() for child in self.children])
    
    def get_edges(self) -> list:
        _, edges = self.__get_edges__(0, 0)
        return edges

    def __get_edges__(self, prev, count) -> int | list:
        if self.children == None:
            return count+1, []
        new_count = count+1
        edges = []
        for child in self.children:
            edges += [(prev, new_count)]
            c, e = child.__get_edges__(new_count, new_count)
            new_count = c
            edges += e
        return new_count, edges
