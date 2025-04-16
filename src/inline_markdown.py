import re
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


def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node_image(node))
    
    return new_nodes

def split_node_image(node):
    result = []
    text = node.text
    images = extract_markdown_images(text)
    if len(images) < 1:
        return [node]

    for image in images:

        split_text = text.split(f"![{image[0]}]({image[1]})", 1)

        if split_text[0] != "":
            result.append(TextNode(split_text[0], TextType.TEXT))

        result.append(TextNode(image[0], TextType.IMAGE, image[1]))

        text = split_text[1]

    if text != "":
        result.append(TextNode(text, TextType.TEXT))
    
    return result




def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node_link(node))
    
    return new_nodes

def split_node_link(node):
    result = []
    text = node.text
    links = extract_markdown_links(text)
    if len(links) < 1:
        return [node]

    for link in links:

        split_text = text.split(f"[{link[0]}]({link[1]})", 1)

        if split_text[0] != "":
            result.append(TextNode(split_text[0], TextType.TEXT))

        result.append(TextNode(link[0], TextType.LINK, link[1]))

        text = split_text[1]

    if text != "":
        result.append(TextNode(text, TextType.TEXT))
    
    return result

