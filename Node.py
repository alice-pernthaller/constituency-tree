
class Node:
    _NextNodeNumber = 0

    def __init__(self, label):
        self.NodeNumber = Node._NextNodeNumber
        Node._NextNodeNumber += 1

        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0

    def __str__(self):
        return f"Node: {self.label}, {self.children}"


def parse(tokens, start, end):
    label = tokens[start+1]
    node = Node(label)

    bracket_level = 0
    start_of_child = None

    position_after_label = start + 2
    position_before_final_bracket = end - 1

    for i in range(position_after_label, position_before_final_bracket):
        token = tokens[i]

        if token == '(':
            if bracket_level == 0:
                start_of_child = i
            bracket_level += 1
            continue

        if token == ')':
            bracket_level -= 1
            if bracket_level == 0:
                child = parse(tokens, start_of_child, i+1)
                node.add_child(child)
                start_of_child = None
            continue

        if bracket_level == 0:
            leaf = Node(token)
            node.add_child(leaf)

    return node


def get_edges(node):
    edges = []

    def _get_edges(node):
        for child in node.children:
            edges.append([node, child])
            _get_edges(child)

    _get_edges(node)
    return edges


def get_nodes(node):
    nodes = []

    def _get_nodes(node):
        nodes.append(node)
        for child in node.children:
            _get_nodes(child)
    _get_nodes(node)
    return nodes


def get_leafs(node):
    nodes = get_nodes(node)
    leafs = []
    for node in nodes:
        if node.is_leaf():
            leafs.append(node)
    return leafs
