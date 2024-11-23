import os
import re

def rename_blocks_to_ans(directory="."):
    """
    Rename all block_x_y.txt files to ans_x_y.txt in the given directory.

    Args:
        directory (str): The directory to scan for files (default is the current directory).
    """
    # Regular expression to match block_x_y.txt
    pattern = re.compile(r"^block_(\d+)_(\d+)\.txt$")
    
    # List all files in the directory
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            # Construct new filename
            new_filename = f"ans_{match.group(1)}_{match.group(2)}.txt"
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    # Call the function in the current directory
    rename_blocks_to_ans()
