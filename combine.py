import json

# Function to parse the manual markdown documentation
# This is a placeholder function. You need to implement parsing based on your markdown structure.
def parse_manual_markdown(file_path):
    documented_commands = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_command = ""
        for line in lines:
            if line.startswith('## Reference for `'):
                current_command = line.split('`')[1].strip()
                documented_commands[current_command] = {"options": []}
            elif line.startswith('- `--'):
                option = line.split('`')[1].strip()
                documented_commands[current_command]["options"].append(option)
    return documented_commands

# Function to generate markdown for undocumented commands and options
def generate_markdown_for_undocumented_commands(json_data, documented_commands):
    markdown_sections = []
    for command, details in json_data.items():
        if command not in documented_commands:
            markdown_sections.append(f"## Reference for `{command}`\n")
            markdown_sections.append(details["synopsis"].replace("\\n", "\n") + "\n")
            markdown_sections.append("### Options\n")
            for option in details["options"]:
                markdown_sections.append(f"- `--{option['option']}`: {option['description']}\n")
        else:
            # Check for undocumented options
            documented_options = documented_commands[command]["options"]
            for option in details["options"]:
                if option["option"] not in documented_options:
                    markdown_sections.append(f"- `--{option['option']}`: {option['description']} (Automatically added)\n")
    return markdown_sections

# Load the JSON commands file
with open('kubernetes.json', 'r') as json_file:
    commands_data = json.load(json_file)

# Parse the manual markdown documentation
manual_documentation_path = 'manual_documentation.md'
documented_commands = parse_manual_markdown(manual_documentation_path)

# Generate markdown for undocumented commands and options
undocumented_markdown = generate_markdown_for_undocumented_commands(commands_data, documented_commands)

# Write the combined markdown to a new file
with open('combined_documentation.md', 'w') as combined_file:
    # First, write the manually documented content
    with open(manual_documentation_path, 'r') as manual_file:
        combined_file.write(manual_file.read())
    
    # Then, append the generated markdown for undocumented commands/options
    combined_file.write("\n".join(undocumented_markdown))

print("Combined documentation generated in 'combined_documentation.md'")
