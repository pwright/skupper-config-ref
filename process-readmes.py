import re
import glob

def process_adoc_files(file_pattern):
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        new_content = []
        skip_contents = False
        step_heading_regex = re.compile(r'^==+\s*Step\s+\d+:')

        for line in content:
            if line.strip() == '[discrete]':
                skip_contents = True
            elif skip_contents and line.strip().startswith('==== Contents'):
                continue
            elif skip_contents and line.strip() == '':
                skip_contents = False
                continue

            if step_heading_regex.match(line):
                step_title = step_heading_regex.sub('', line).strip()
                new_content.append(f". {step_title}\n+\n--\n")
            elif new_content and new_content[-1].endswith("--\n"):
                if line.strip() == '':
                    new_content[-1] = new_content[-1][:-1] + line
                else:
                    new_content.append(line)
            else:
                new_content.append(line)

            if line.strip() == '':
                if new_content and new_content[-1].endswith("--\n"):
                    new_content[-1] = new_content[-1] + "--\n"

        with open(file_path, 'w') as file:
            file.writelines(new_content)

# Replace 'your_path/*.adoc' with the actual pattern matching your AsciiDoc files.
process_adoc_files('examples/*.adoc')
