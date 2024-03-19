import os
import glob

def insert_links_to_list_items(asciidoc_content, filename):
    """
    Inserts inline anchors for each numbered list item in an AsciiDoc document and
    places a list of links just before the first list item. Ensures there is a new
    line after the list of links. Removes all periods from filenames in anchors and
    links, and ensures anchors are placed inline with the numbered list items.

    Args:
    - asciidoc_content (str): The content of the AsciiDoc file.
    - filename (str): The name of the AsciiDoc file, used in anchors and links,
                      with periods removed.
    """
    lines = asciidoc_content.split('\n')
    updated_content = []
    links = []
    list_item_count = 0
    filename_no_periods = filename.replace('.', '')

    first_list_item_index = None

    for i, line in enumerate(lines):
        if line.startswith('. '):
            list_item_count += 1
            item_text = line[2:].strip()
            anchor = f"{filename_no_periods}_item{list_item_count}"
            link = f"* xref:{anchor}[{item_text}]"
            links.append(link +'\n')
            updated_line = f". [[{anchor}]]{item_text}"
            lines[i] = updated_line  # Update the line in place
            if first_list_item_index is None:
                first_list_item_index = i

    # Inserting links and a newline after the list of links, before the first list item
    if first_list_item_index is not None:
        for link in reversed(links):
            lines.insert(first_list_item_index, link)
        lines.insert(first_list_item_index, '')  # Add a newline before the list of links

    return '\n'.join(lines)

def process_files_in_directory(directory_path='examples'):
    """
    Processes all AsciiDoc files in the specified directory, overwriting them
    with the updated content that includes inline anchors and links for each list item.
    Ensures that links appear just before the first list item and that there is a new
    line after the list of links.
    """
    adoc_pattern = os.path.join(directory_path, '*.adoc')
    adoc_files = glob.glob(adoc_pattern)

    for file_path in adoc_files:
        filename = os.path.splitext(os.path.basename(file_path))[0]
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = insert_links_to_list_items(content, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

# Invoke the function to process files in the 'examples' directory
process_files_in_directory()
