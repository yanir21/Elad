def format_nodes(nodes_from_db):
    for intent in nodes_from_db:
        add_patterns_to_father_node(intent)

def add_patterns_to_father_node(node):
    node_patterns = node.patterns

def _finditem(obj, key):
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            item = _finditem(v, key)
            if item is not None:
                return item


def tree_traverse(tree, key):
    for k, v  in tree.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            found = tree_traverse(v, key) 
            if found is not None:  # check if recursive call found it
                return found

def get_node_by_id(node, id):
    if node["id"] == id:
        return node
    elif "children" in node:
        for child in node["children"]:
            get_node_by_id(child, id)
    else:
        return None