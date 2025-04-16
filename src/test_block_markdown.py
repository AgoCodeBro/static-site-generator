import unittest
from block_markdown import *

class TestBlock(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype(self):
            
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

> This
>is a quote

- This
-Should
- Not be a list

``` This should be code
no matter what
```

```
this is
also code
```

1. this
2. should
3. be ordered

2. this
3. should be para

1. so
3. should
4. this

#Not a heading

# a heading

### a also a heading

###### still a heading

####### Not a  heading

###Also Not a heading
    """
            blocks = markdown_to_blocks(md)
            # p p u q p c c o p p p h h h p
            BlockType.PARAGRAPH,
            BlockType.UNORDERED_LIST,
            BlockType.CODE,
            BlockType.HEADING,
            BlockType.ORDERED_LIST,
            BlockType.QUOTE,
            expected_result = [BlockType.PARAGRAPH,
                               BlockType.PARAGRAPH,
                               BlockType.UNORDERED_LIST,
                               BlockType.QUOTE,
                               BlockType.PARAGRAPH,
                               BlockType.CODE,
                               BlockType.CODE,
                               BlockType.ORDERED_LIST,
                               BlockType.PARAGRAPH,
                               BlockType.PARAGRAPH,
                               BlockType.PARAGRAPH,
                               BlockType.HEADING,
                               BlockType.HEADING,
                               BlockType.HEADING,
                               BlockType.PARAGRAPH,
                               BlockType.PARAGRAPH,
                               ]
            
            result = []
            blocks = markdown_to_blocks(md)
            for block in blocks:
                result.append(block_to_blocktype(block))
            for i in range(len(result)):
                 print()
                 print(f"Expected:{expected_result[i]}  Actual:{result[i]}")
                 print()
            self.assertEqual(result, expected_result)