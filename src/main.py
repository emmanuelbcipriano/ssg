import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    # Define paths
    content_dir = "content"
    template_path = "template.html"
    dest_dir = "docs"  # Changed from "public" to "docs"

    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


    generate_pages_recursive(
    content_dir,  # Directory containing Markdown files
    template_path,  # Path to the HTML template
    dest_dir,  # Directory where HTML files will be saved
    basepath
)


main()
