from pathlib import Path
FILENAME = 'ADA.txt'
file_contents = Path(FILENAME).read_text()
file_contents = file_contents[file_contents.find('\n') +1:].replace('\n', '')
print(len(file_contents))