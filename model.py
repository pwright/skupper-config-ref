import re
import os
import glob
import argparse
import json

class CommandModel:
    def __init__(self):
        self.commands = {}

    def add_command(self, command_name, synopsis=""):
        if command_name not in self.commands:
            self.commands[command_name] = {"synopsis": synopsis, "options": []}

    def add_option(self, command_name, option, option_type, description):
        if command_name in self.commands:
            self.commands[command_name]["options"].append({"option": option, "type": option_type, "description": description})

    def parse_markdown_file(self, file_path):
        with open(file_path, 'r') as file:
            markdown_content = file.read()
            self.parse_markdown_content(markdown_content)

    def parse_markdown_content(self, markdown_content):
        lines = markdown_content.split("\n")
        current_command = ""
        synopsis_mode = False
        synopsis_content = []
        for line in lines:
            command_match = re.match(r"^##\s+(.*)$", line)
            synopsis_start_match = re.match(r"^###\s+Synopsis$", line)
            heading_match = re.match(r"^###\s+", line)
            option_match = re.match(r"^\s{6}--(\w+)(?:\s+(\w+))?\s+(.*)$", line)

            if command_match:
                if current_command and synopsis_content:
                    self.commands[current_command]["synopsis"] = "\\n".join(synopsis_content).strip()
                    synopsis_content = []
                current_command = command_match.group(1).strip()
                synopsis_mode = False
                self.add_command(current_command)
            elif synopsis_start_match:
                synopsis_mode = True
            elif synopsis_mode and not heading_match:
                synopsis_content.append(line.strip())
            elif heading_match and synopsis_mode:
                self.commands[current_command]["synopsis"] = "\\n".join(synopsis_content).strip()
                synopsis_content = []
                synopsis_mode = False
            elif option_match:
                option = option_match.group(1).strip()
                option_type = option_match.group(2) if option_match.group(2) else "flag"
                description = option_match.group(3).strip()
                self.add_option(current_command, option, option_type, description)

        if current_command and synopsis_content:
            self.commands[current_command]["synopsis"] = "\\n".join(synopsis_content).strip()

    def get_model(self):
        return self.commands

def process_markdown_directory(directory_path):
    model = CommandModel()
    for file_path in glob.glob(os.path.join(directory_path, '*.md')):
        model.parse_markdown_file(file_path)
    return model.get_model()

def main():
    parser = argparse.ArgumentParser(description="Process markdown files to extract commands, synopses, and options, encoding new lines in synopsis.")
    parser.add_argument('directory', type=str, help='Directory containing markdown files.')
    args = parser.parse_args()

    commands_model = process_markdown_directory(args.directory)
    # Convert the commands model to JSON format
    json_output = json.dumps(commands_model, indent=4)
    print(json_output)

if __name__ == "__main__":
    main()
