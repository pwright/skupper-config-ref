import re
import glob

def process_adoc_files(file_pattern):
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        new_content = []
        skip_contents = False
        step_content=False
        step_heading_regex = re.compile(r'^==+\s*Step\s+\d+:')
        section_name_regex = re.compile(r'_\*(.*):\*_')


        for line in content:
            if line.strip() == '[discrete]':
                skip_contents = True
            elif skip_contents and line.strip().startswith('==== Contents'):
                continue
            elif skip_contents and line.strip().startswith('* <<'):
                continue
            elif skip_contents and line.strip() == '== Overview':
                skip_contents = False
                continue

            if section_name_regex.match(line):
                section_name= section_name_regex.search(line).group(1)
                line= section_name

            if step_heading_regex.match(line):
                step_title = step_heading_regex.sub('', line).strip()
            
                line = ". " + step_title+"\n+\n--\n"
                step_content= True
            
            if line.strip().startswith('. ') and step_content==True:
                
                line =  "--\n" + line
                step_content= False

            new_content.append(line)

        with open(file_path, 'w') as file:
            file.writelines(new_content)
process_adoc_files('examples/*.adoc')
