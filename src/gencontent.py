import os
from markdown_blocks import markdown_to_html_node




def generate_page(markdown_path, template_path, html_dest_path, basepath):
    # Read the Markdown file
    with open(markdown_path, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    # Convert Markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Read the template
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    # Replace placeholders in the template
    final_html = template.replace("{{ Title }}", os.path.basename(markdown_path))
    final_html = final_html.replace("{{ Content }}", html)

    # Replace href="/ and src="/ with the basepath
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    # Write the final HTML to the destination file
    with open(html_dest_path, 'w', encoding='utf-8') as html_file:
        html_file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # Ensure the destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    # Iterate over all entries in the content directory
    for entry in os.listdir(dir_path_content):
        # Construct full paths
        content_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(content_path):
            # If it's a directory, recursively process it
            generate_pages_recursive(content_path, template_path, dest_path, basepath)
        elif entry.endswith(".md"):
            # If it's a markdown file, generate the corresponding HTML file
            html_filename = os.path.splitext(entry)[0] + ".html"
            html_dest_path = os.path.join(dest_dir_path, html_filename)
            generate_page(content_path, template_path, html_dest_path, basepath)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
