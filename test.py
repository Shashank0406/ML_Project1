import os

print(os.getcwd())

def check_directory_permissions(directory_path):
    if os.access(directory_path, os.W_OK):
        print(f"The directory '{directory_path}' has write permissions.")
    else:
        print(f"The directory '{directory_path}' does not have write permissions.")

# Example usage
directory_to_check = os.getcwd()
check_directory_permissions(directory_to_check)
