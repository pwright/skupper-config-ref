import json
import argparse
import os

# Set up argument parsing
parser = argparse.ArgumentParser(description="Merge manual AsciiDoc documentation with JSON command details.")
parser.add_argument("asciidoc_file", help="Input manual documentation AsciiDoc filename")
parser.add_argument("json_file", help="JSON file containing command details")
args = parser.parse_args()

# Function to parse manual AsciiDoc documentation
def parse_manual_asciidoc(file_path):
    documented_commands = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_command = ""
        for line in lines:
            line = line.strip()  # Remove leading and trailing whitespace
            if line.startswith('== Reference for '):
                current_command = line.split('`')[1].strip()
                documented_commands[current_command] = {"options": [], "documented": True}
            elif line.startswith('-'):
                option = line.split('`')[1].strip()
                documented_commands[current_command]["options"].append(option)
    return documented_commands

# Function to generate AsciiDoc for commands and options
def generate_asciidoc(json_data, documented_commands):
    asciidoc_sections = []
    for command, details in json_data.items():
        if command in documented_commands:
            # Add commented synopsis and options for manually documented commands
            asciidoc_sections.append(f"// Manually documented: {command}")
            asciidoc_sections.append(f"// Synopsis: {details['synopsis'].replace('\\n', ' ').strip()}")
            if details["options"]:  # Check if there are options to document
                asciidoc_sections.append("// *Options:*")
            for option in details["options"]:
                asciidoc_sections.append(f"// * `--{option['option']}`: {option['description'].strip()}")
        else:
            # Add undocumented commands with synopsis and options
            asciidoc_sections.append(f"== Reference for `{command}`")
            synopsis = details['synopsis'].replace('\\n', ' ').strip()
            if synopsis:  # Ensure synopsis doesn't start with space
                asciidoc_sections.append(synopsis)
            if details["options"]:  # Ensure a line break before starting the options
                asciidoc_sections.append("\n*Options:*")
            for option in details["options"]:
                option_line = f"* `--{option['option']}`: {option['description'].strip()}"
                asciidoc_sections.append(option_line)
    return asciidoc_sections

# Load the JSON commands file
with open(args.json_file, 'r') as json_file:
    commands_data = json.load(json_file)

# Parse the manual AsciiDoc documentation
documented_commands = parse_manual_asciidoc(args.asciidoc_file)

# Generate AsciiDoc for commands and options
undocumented_asciidoc = generate_asciidoc(commands_data, documented_commands)

# Construct the output filename from the input filename
base_name = os.path.splitext(args.asciidoc_file)[0]
output_file = f"{base_name}-out.adoc"

# Write the combined AsciiDoc to the derived output file
with open(output_file, 'w') as combined_file:
    # First, write the manually documented content
    with open(args.asciidoc_file, 'r') as manual_file:
        combined_file.write(manual_file.read().strip() + '\n\n')  # Ensure no leading spaces in manual content
    
    # Then, append the generated AsciiDoc for commands/options, ensuring proper line breaks and formatting
    combined_content = '\n'.join(undocumented_asciidoc).strip()
    combined_file.write(combined_content)

print(f"Combined documentation generated in '{output_file}'")
