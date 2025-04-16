from enum import Enum

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
        print()
        print(line)
        print()
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
