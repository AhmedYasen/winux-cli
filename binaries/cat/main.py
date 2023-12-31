import sys

def cat(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cat <file_path>")
    else:
        file_path = sys.argv[1]
        cat(file_path)
