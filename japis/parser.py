import sys

def compare_files(input_file, template_file='/home/user/git/labs/japis/lab3/template.txt'):
    try:
        with open(input_file, 'r', encoding='utf-8') as input_f:
            input_lines = input_f.readlines()

        with open(template_file, 'r', encoding='utf-8') as template_f:
            template_lines = template_f.readlines()

        max_lines = max(len(input_lines), len(template_lines))
        differences_found = False

        # Compare line by line
        for i in range(max_lines):
            input_line = input_lines[i] if i < len(input_lines) else None
            template_line = template_lines[i] if i < len(template_lines) else None

            if input_line != template_line:
                if template_line.strip() == 'idAttr = node.getAttribute("id")':
                    print("Variable idAttr is not defined")
                elif template_line.strip() == 'xmlDoc = parseXML(xmlString)':
                    print(f"Unexpected function parse()")
                elif template_line.strip() == 'nodes = root.children()':
                    print(f"Unexpected method childrens()") 
                else:
                    print(f"Unexpected error at line {i + 1}")
                return
        if not differences_found:
            print("No errors detected.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main(input_file):
    # Compare the input file with the template
    compare_files(input_file)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python parser.py <input_file_name>")
