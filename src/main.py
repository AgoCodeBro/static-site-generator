from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode
import os
import os.path as osp
import shutil
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 0:
        basepath = sys.argv[0]
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


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


def generate_page(from_path, template_path, dest_path, basepath):
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

    result = result.replace('href="/', f'href="{basepath}')
    result = result.replace('src="/', f'src="{basepath}')
    
    dir_name = osp.dirname(dest_path)

    os.makedirs(dir_name, exist_ok=True)

    file = open(dest_path, "w")
    file.write(result)

    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not (osp.exists(dir_path_content) and osp.isdir(dir_path_content)):
        raise ValueError("Please provide a valid path to the content directory")
    
    if not osp.exists(template_path):
        raise ValueError("Please provide a valid path to the template")
    
    content = os.listdir(dir_path_content)
    
    for item in content:
        source = osp.join(dir_path_content, item)
        destination = osp.join(dest_dir_path, item)
        if osp.isdir(source):
            generate_pages_recursive(source, template_path, destination, basepath)

        elif osp.isfile(source):
            if item[-3:] == ".md":
                generate_page(source, template_path, f"{destination[:-3]}.html", basepath)



if __name__ == "__main__":
    main()