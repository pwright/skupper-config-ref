import os
import yaml
import re

def load_mappings(filepath):
    """Load and return mappings from a YAML file."""
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data.get('simple_mappings', {}), data.get('regex_mappings', [])

def apply_simple_mappings(text, simple_mappings):
    """Apply simple text replacements."""
    for old, new in simple_mappings.items():
        text = text.replace(old, new)
    return text

def apply_regex_mappings(text, regex_mappings):
    """Apply regex mappings to the given text."""
    for mapping in regex_mappings:
        pattern = mapping['pattern']
        replacement = mapping['replacement']
        text = re.sub(pattern, replacement, text)
    return text

def apply_mappings(text, simple_mappings, regex_mappings):
    """Apply both simple and regex mappings."""
    text = apply_simple_mappings(text, simple_mappings)
    text = apply_regex_mappings(text, regex_mappings)
    return text

def process_file(file_path, simple_mappings, regex_mappings):
    """Process a single file, applying the mappings."""
    with open(file_path, 'r') as file:
        content = file.read()
    modified_content = apply_mappings(content, simple_mappings, regex_mappings)
    with open(file_path, 'w') as file:
        file.write(modified_content)

def process_directory(directory_path, simple_mappings, regex_mappings):
    """Process all files in the given directory."""
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.amd') or file_name.endswith('.adoc'):
                file_path = os.path.join(root, file_name)
                process_file(file_path, simple_mappings, regex_mappings)

# Load mappings
simple_mappings, regex_mappings = load_mappings('mappings.yaml')

# Process directories
process_directory('examples/', simple_mappings, regex_mappings)
process_directory('/path/to/asciidoc/files', simple_mappings, regex_mappings)
