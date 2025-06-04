with open ('file1.txt', 'r') as reader:
    content = reader.readlines()
    line_count = len(content)
print(f"Total number of lines: {line_count}")