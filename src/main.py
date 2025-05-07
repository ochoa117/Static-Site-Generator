from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node, extract_title
import os, shutil
from pathlib import Path

def main():

    static_to_public_copy(
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/static",
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/public"
    )

    generate_pages_recursive(
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/content",
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/template.html",
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/public"
    )

    

def delete_directory_contents(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def static_to_public_copy(src, dst):
    delete_directory_contents(dst)
    for filename in os.listdir(src):
        file_path = os.path.join(src, filename)
        try:
            if os.path.isdir(file_path):
                new_dst = os.path.join(dst, os.path.basename(file_path))
                os.mkdir(new_dst)
                static_to_public_copy(file_path, new_dst)
            else:
                shutil.copy(file_path, dst)
        except Exception as e:
            print(f"Failed to copy {file_path}. Reason: {e}")
    
def generate_path(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file_content = ""
    temp_content = ""
    # Automatically closes files
    with open(from_path) as file:
        file_content = file.read()
    with open(template_path) as temp:
        temp_content = temp.read()
    file_html = markdown_to_html_node(file_content).to_html()
    file_title = extract_title(file_content)
    new_temp_content = temp_content.replace("{{ Title }}", file_title).replace("{{ Content }}", file_html)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as dest:
        dest.write(new_temp_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    new_dest_file = Path("index.html")
    for content in contents:
        content_path = os.path.join(dir_path_content, content)
        if not os.path.isfile(content_path):
            generate_pages_recursive(content_path, template_path, os.path.join(dest_dir_path, content))
        else:
            new_dest_dir_path = os.path.join(dest_dir_path, new_dest_file)
            generate_path(content_path, template_path, new_dest_dir_path)

main()