import argparse
import os
import re

def extract_first_heading(markdown_content):
    # Updated regex to match the first heading of any level
    first_heading_regex = r'^#{1,6}\s+(.*)'
    match = re.search(first_heading_regex, markdown_content, re.MULTILINE)
    if match:
        print(f"Found section title: {match.group(1).strip()}")  # Debugging output
        return match.group(1).strip()
    print("No section title found.")  # Debugging output for troubleshooting
    return "Untitled"

def extract_options_from_markdown(markdown_content):
    options_start_regex = r'#+\s+Options'
    match = re.search(options_start_regex, markdown_content)
    if not match:
        print("No options section found.")  # Debugging output
        return "", ""  # No options section found
    options_start_index = match.start()
    options_content = markdown_content[options_start_index:]
    # Extract the first heading before the options section as title
    title = extract_first_heading(markdown_content[:options_start_index])
    return title, options_content

def format_options_as_adoc(title, options_content):
    option_regex = r'^\s*(--[\w-]+)\s+([\w]+)?\s*(.*)$'
    adoc_content = f"== {title}\n\n"
    ignore_options = ['--kubeconfig', '--platform']  # List of options to ignore

    for line in options_content.split('\n'):
        match = re.match(option_regex, line.strip())
        if match:
            option_name = match.group(1)
            # Skip processing for ignored options
            if option_name in ignore_options:
                continue  # Skip this option and proceed with the next iteration

            description = match.group(3).strip()
            # Start the block
            option_block = f"{option_name}::\n+\n--\n"
            
            # Check for option patterns in the description and format as bullet list
            options_list_match = re.search(r'\[([^\]]+)\]', description)
            if options_list_match:
                # Extract and format the options list
                options_list = options_list_match.group(1).split('|')
                formatted_list = "\n".join([f"* {opt.strip()}" for opt in options_list])
                # Append the formatted list at the end of the description
                description += f"\n\nOptions include:\n\n{formatted_list}"
            
            # Append the description to the block
            option_block += f"{description}\n--\n\n"
            # Update the AsciiDoc content with the formatted block
            adoc_content += option_block

    return adoc_content


def convert_markdown_to_adoc(directory_path):
    adoc_file_content = ""
    for filename in os.listdir(directory_path):
        if filename.endswith(".md"):
            print(f"Processing file: {filename}")  # Indicate which file is being processed
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                markdown_content = file.read()
                title, options_content = extract_options_from_markdown(markdown_content)
                if options_content:
                    adoc_content = format_options_as_adoc(title, options_content)
                    adoc_file_content += adoc_content
                else:
                    print(f"No options section found in {filename}")  # Debugging output
    return adoc_file_content

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown options to AsciiDoc format with headings.")
    parser.add_argument("directory", type=str, help="Directory containing Markdown files")

    args = parser.parse_args()
    directory_path = args.directory

    adoc_content = convert_markdown_to_adoc(directory_path)

    # Write the AsciiDoc content to a file
    output_file_path = os.path.join(directory_path, "options.adoc")
    with open(output_file_path, 'w') as adoc_file:
        adoc_file.write(adoc_content)
    print(f"AsciiDoc options file created at: {output_file_path}")

if __name__ == "__main__":
    main()
