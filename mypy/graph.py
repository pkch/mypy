class Graph:
    class Node:
        '''
        One node belongs only to one graph
        (although of course it's ok to share values)
        So it's pretty arbirary whether to have add_edge/remove_edge here or in Graph
        '''
        def __init__(self, value=None):
            '''
            Only graph instance should create Node
            '''
            self.value = value
            self.outgoing = set()
            self.incoming = set()

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return str(self.value) + '->' + ' '.join(map(str, self.outgoing))

    def __init__(self):
        self.nodes = set()

    def __iter__(self):
        return iter(self.nodes)

    def add_node(self, value=None):
        n = self.Node(value)
        self.nodes.add(n)
        return n

    def add_edge(self, v, w):
        v.outgoing.add(w)
        w.incoming.add(v)

    def remove_edge(self, v, w):
        v.outgoing.remove(w)
        w.incoming.remove(v)

    def __str__(self):
        return '\n'.join(map(repr, self.nodes))
