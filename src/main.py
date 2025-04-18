from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode
import os
import os.path as osp
import shutil

def main():
    copy_directory("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if len(line) < 2:
            continue

        elif line[0] == "#" and line[1] != "#":
            return line[1:].strip()

    raise ValueError("Markdown file has no title. Please ensure there is an h1 header")


def copy_directory(source, destination):
    if not osp.exists(source):
        raise ValueError("Source path not found")

    if osp.exists(destination):
        try:
            shutil.rmtree(destination)

        except:
            raise ValueError("Destination given should be a directory")
        
    
    os.mkdir(destination)
    source_content = os.listdir(source)
    for item in source_content:
        item_path = f"{source}/{item}"

        if osp.isfile(item_path):
            shutil.copy(item_path, destination)

        elif osp.isdir(item_path):
            copy_path = f"{destination}/{item}"
            os.mkdir(copy_path)
            copy_directory(item_path, copy_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    try:
        source = open(from_path)
        markdown = source.read()

    except Exception as e:
        raise ValueError("Unable to open file. Please provide a valid from path to a valid file")
    
    try:
        source = open(template_path)
        template = source.read()

    except Exception as e:
        raise ValueError("Unable to open file. Please provide a valid template path to a valid file")
    
    title = extract_title(markdown)

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    template = template.replace("{{ Title }}", title)
    result = template.replace("{{ Content }}", html)
    
    dir_name = osp.dirname(dest_path)

    os.makedirs(dir_name, exist_ok=True)

    file = open(dest_path, "w")
    file.write(result)

    



if __name__ == "__main__":
    main()