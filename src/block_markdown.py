from enum import Enum
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnode

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered List"
    ORDERED_LIST = "Ordered List"

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    result = []
    for block in raw_blocks:
        block = block.strip()
        if block != "":
            result.append(block)



    return result


def block_to_blocktype(block):
    # If line starts with # verify that there are 1-6 # and followed by a space and a character
    if block[0] == "#":
        count = 0
        for i in block:
            if i == "#":
                count += 1

            else:
                break
        
        # > count +1 so its all the #s plus a space plus a character
        if count <= 6 and len(block) > (count + 1) and block[count] == " ":
            return BlockType.HEADING
        
        # If the line starts with # and isnt a Heading its a paragraph
        else:
            return BlockType.PARAGRAPH

    # if block starts and ends with "```" its code. If it only starts with it, its a paragraph  
    elif block[:3] == "```":

        if block[-3:] == "```":
            return BlockType.CODE
        
        else:
            return BlockType.PARAGRAPH

    lines = block.split("\n")
    isUnordered = True
    isOrdered = True
    isQuote = True
    num = 1

    for line in lines:
        x = line[0]
        y = line [1]

        #if line doesnt start with ">" its not a quote
        if x != ">":
            isQuote = False
        
        #if line doesnt start with "- " its not an unordered list
        if x != "-" or y != " ":
            isUnordered = False

        #if line doesnt start with a "x." where x is a digit its not an ordered list
        if x.isdigit() == False or y != "." :
            isOrdered = False
        
        elif int(x) != num:
            isOrdered = False
        
        num += 1

    if isOrdered:
        return BlockType.ORDERED_LIST
    
    elif isUnordered:
        return BlockType.UNORDERED_LIST
    
    elif isQuote:
        return BlockType.QUOTE
    
    #If its none of the above, its a paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_of_head_node = []
    
    for block in blocks:
       node = block_to_html_node(block)
       children_of_head_node.append(node)
    
    return ParentNode("div", children_of_head_node)

def block_to_html_node(block):
    #This function just selects the correct node builder for the block type

    converters = {BlockType.PARAGRAPH : paragraph_to_html_node,
                  BlockType.HEADING : heading_to_html_node,
                  BlockType.CODE : code_to_html_node,
                  BlockType.QUOTE : quote_to_html_node,
                  BlockType.UNORDERED_LIST : ulist_to_html_node,
                  BlockType.ORDERED_LIST : olist_to_html_node,
                  }
    
    block_type = block_to_blocktype(block)

    # Uses block_type to select the correct function from the dictionary
    return converters[block_type](block)
    
def paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)

    return ParentNode("p", children)

def heading_to_html_node(block):
    count = 0

    while block[count] == "#":
        count += 1
    
    text = block[count + 1:]
    children = text_to_children(text)

    return ParentNode(f'h{count}', children)

def code_to_html_node(block):
      text = block[4:-3]
      text_node = TextNode(text, TextType.TEXT)
      children  = [text_node_to_html_node(text_node)]
      code_node = ParentNode("code", children)

      return ParentNode("pre", [code_node])

def quote_to_html_node(block):
    raw_text = block.split("\n")
    lines = []
    for line in raw_text:
        plain_line = line.strip(">")
        lines.append(plain_line.strip())
    text = " ".join(lines)
    children = text_to_children(text)

    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    raw_text = block.split("\n")
    children = []
    for line in raw_text:
        child_node = text_to_children(line[2:])
        children.append(ParentNode("li", child_node))

    return ParentNode("ul", children)

def olist_to_html_node(block):
    raw_text = block.split("\n")
    children = []
    for line in raw_text:
        child_node = text_to_children(line[3:])
        children.append(ParentNode("li", child_node))

    return ParentNode("ol", children)

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))

    return children