from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            results += node
        
        else:
            raw_texts = node.text.split(delimiter)
            isText = True
            if len(raw_texts) % 2 != 1:
                raise Exception("no closing delimeter found")
            for text in raw_texts:
                if isText:
                    new = TextNode(text, TextType.TEXT)
                    results.append(new)

                else:
                    new = TextNode(text, text_type)
                    results.append(new)

                isText = not isText

    return results