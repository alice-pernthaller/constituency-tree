import Node
import graphviz


def pretty_print(root):
    nodes = Node.get_nodes(root)
    leafs = filter(lambda n: n.is_leaf(), nodes)
    non_leafs = filter(lambda n: not n.is_leaf(), nodes)

    g = graphviz.Digraph(filename='cake_spoon', format='svg')

    with g.subgraph() as s:
        s.attr(rank='same')
        for leaf in leafs:
            s.node(str(leaf.NodeNumber), label=leaf.label, shape='box', style='filled', fillcolor='mistyrose')
    for node in non_leafs:
        g.node(str(node.NodeNumber), label=node.label, shape='box', style='filled', fillcolor='lightcyan')

    edges = Node.get_edges(root)
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        g.edge(str(parent.NodeNumber), str(child.NodeNumber), arrowsize="0.7", arrowhead='open')

    g.view()
