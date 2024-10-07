import os
import sys

def count_lines(path, extensions):
  os.chdir(path)
  lines = 0
  
  for file in os.listdir():
    if any(file.endswith(ext) for ext in extensions):
      with open(file, 'r') as f:
        file_lines = sum(1 for line in f)
      lines += file_lines
      print(f"file: {file} +{file_lines}")
  print(f'You wrote a total of {lines} lines of code')

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print("Usage: python3 count_lines.py <path> <extensions...>")
    print("Example: python3 count_lines.py /home/Desktop .c .cpp .hpp")
    sys.exit(1)
    
  count_lines(sys.argv[1], sys.argv[2:])
