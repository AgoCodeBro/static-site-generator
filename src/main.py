from textnode import TextNode, TextType
import os
import os.path as osp
import shutil

def main():
    copy_directory("static", "public")

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



            
    



if __name__ == "__main__":
    main()