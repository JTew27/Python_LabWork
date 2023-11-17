#unix wc
import sys
def analyse(file1):
    try:
        with open(file1, 'r') as file:
            content = file.read()

            char_count = len(content)
            word_count = len(content.split())
            space_count = content.count(' ')
            line_count = content.count('\n')

            print("Character count:", char_count)
            print("Word count:", word_count)
            print("Space count:", space_count)
            print("Line count:", line_count)

    except:
        print("File not found!")


# Usage
file1 = sys.argv[1]
analyse(file1)