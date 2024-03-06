import configparser
import os

def should_remove_section(line, sections_to_remove):
    """Check if the current line indicates the start of a section to remove."""
    if line.startswith('#'):
        section_title = line.strip('# ').strip()
        if section_title in sections_to_remove:
            return True
    return False

def get_heading_level(line):
    """Return the heading level (number of '#' characters) of a line, or 0 if not a heading."""
    if line.startswith('#'):
        return line.count('#')
    return 0

def remove_sections(md_file_path, sections_to_remove):
    """Remove specified sections from a Markdown file."""
    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    skip_section = False
    current_section_level = 0

    for line in lines:
        if line.startswith('#'):
            heading_level = get_heading_level(line)
            if should_remove_section(line, sections_to_remove):
                skip_section = True
                current_section_level = heading_level
                continue
            elif skip_section and heading_level <= current_section_level:
                # Exiting the current section
                skip_section = False
                current_section_level = 0

        if not skip_section:
            new_lines.append(line)

    return ''.join(new_lines)

config = configparser.ConfigParser()
config.read('sections.ini')
sections_to_remove = config['remove']['sections'].split(', ')

md_dir = 'examples'
md_files = [os.path.join(md_dir, f) for f in os.listdir(md_dir) if f.endswith('.md')]

for md_file in md_files:
    modified_content = remove_sections(md_file, sections_to_remove)
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    print(f"Processed {md_file}")
