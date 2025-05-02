from textnode import TextNode, TextType
import os, shutil

def main():
    obj = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    obj_str = obj.__repr__()
    print(obj_str)

    static_to_public_copy(
        "/home/minavina96/workspace/github.com/ochoa117/Static-Site-Generator/static",
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


main()