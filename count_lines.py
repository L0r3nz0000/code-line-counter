import os
import sys

def count_lines_in_file(file):
  with open(file, 'r') as f:
    file_lines = sum(1 for line in f)
  return file_lines

def list_files(path, extensions):
  if not os.path.isdir(path):
    return []
  else:
    path = os.path.abspath(path)
  files = []
  
  for file in os.listdir(path):
    if os.path.isdir(file):
      files.extend(list_files(os.path.abspath(file), extensions))
            
    if any(file.endswith(ext) for ext in extensions):
      files.append(os.path.abspath(os.path.join(path, file)))
      
  return files

def print_total_lines(path, extensions):
  path = os.path.abspath(path)
  os.chdir(path)
  files = list_files(path, extensions)
  
  total_lines = 0
  
  for file in files:
    file_lines = count_lines_in_file(file)
    total_lines += file_lines
    
    print(f"file: {file} +{file_lines}")
  print(f'You wrote a total of {total_lines} lines of code')

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print(f"Usage: python3 {sys.argv[0]} <path> <extensions...>")
    print(f"Example: python3 {sys.argv[0]} /home/Project .cpp .h .hpp")
    sys.exit(1)
    
  print_total_lines(sys.argv[1], sys.argv[2:])
