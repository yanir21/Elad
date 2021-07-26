def format_nodes(nodes_from_db):
    for intent in nodes_from_db:
        add_patterns_to_father_node(intent)

def add_patterns_to_father_node(node):
    node_patterns = node.patterns

def get_node_by_id(node, id):
    if node["id"] == id:
        return node
    elif "children" in node:
        for child in node["children"]:
            get_node_by_id(child, id)
    else:
        return None