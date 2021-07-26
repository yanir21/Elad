
bla = {
    "id": 1,
    "tag": "grandfather",
    "patterns": [
        "balas",
        "harmatz"
    ],
    "children": [
         {
            "id": 55,
            "tag": "uncle-girl",
            "patterns": [
                "uncle-girl"
            ],
             "children": [
                {
                    "id": 5,
                    "tag": "idiot",
                    "patterns": [
                        "bla"
                    ]
                }
            ]
        },
        {
            "id": 85,
            "tag": "uncle-girl",
            "patterns": [
                "uncle-girl"
            ],
             "children": [
                {
                    "id": 9,
                    "tag": "idiot",
                    "patterns": [
                        "bla"
                    ]
                }
            ]
        }
    ]
}

def format_node_patterns(node):
    if "children" in node:
        patterns = []
        for child in node["children"]:
            node["patterns"].extend(format_node_patterns(child))
            patterns = node["patterns"]

        return patterns
    else:
        return node["patterns"]

def get_node_by_key(node, key, value, booli):

    tempNode = None
    
    if node[key] == value:
        booli = True
        tempNode = node

    if "children" in node and not booli:
        for child in node["children"]:
            tempNode = get_node_by_key(child, key, value, booli)
    
    return tempNode


def searchTree(element, key, value):
    if element[key] == value:
        return element
    elif element["children"]:
        result = None
        for i in range(len(element["children"])):
            if not result:
                result = searchTree(element["children"][i], key, value)
        return result
    return None

def main():
    node = get_node_by_key(bla, 'id', 9, False)
    #format_node_patterns(bla) 
    print(node)

if __name__ == "__main__":
    main()    