import random
import os

def count_lines_in_file(filename):
    """
    Count the number of lines in a given file.
    
    Args:
        filename (str): The name of the file to count lines.
    
    Returns:
        int: The number of lines in the file.
    """
    with open(filename, 'r') as file:
        return sum(1 for _ in file)


def get_data_width(block_file, y):
    """
    Get the width (number of digits) of a specific data field in a block file.
    
    Args:
        block_file (str): The block file name.
        y (int): The index of the data field.
    
    Returns:
        int: The width (number of digits) of the data field.
    """
    with open(block_file, 'r') as file:
        lines = file.readlines()
        data_line = lines[y]  # Line y corresponds to <data y>.
        value = data_line.split(":")[1].strip()
        return len(value)


def append_x_y_z(in_file):
    """
    Append x, y, z values to the given .in file based on the q value.
    
    Args:
        in_file (str): The name of the .in file to process.
    """
    # Read the input file and parse n, q, and block file names
    with open(in_file, 'r') as file:
        lines = file.readlines()
    
    n, q = map(int, lines[0].split())  # First line: n and q
    block_files = [line.strip() for line in lines[1:n + 1]]  # Block files

    # Generate and append x, y, z values
    with open(in_file, 'a') as file:
        for _ in range(q):
            # Randomly select x (1 <= x <= n)
            x = random.randint(1, n)
            block_file = block_files[x - 1]

            # Determine the number of data lines (k) in the selected block file
            k = count_lines_in_file(block_file) - 2  # Subtract 2 for P and N lines
            y = random.randint(1, k)  # Randomly select y (1 <= y <= k)

            # Get the data width from the selected line in the block file
            data_width = get_data_width(block_file, y)
            
            # Generate a z value with the same number of digits as the selected data
            z = ''.join(random.choices('0123456789', k=data_width))

            # Append the generated x, y, z to the .in file
            file.write(f"{x} {y} {z}\n")


def main():
    # Process files from 2.in to 9.in
    for i in range(0, 10):
        in_file = f"{i}.in"
        if os.path.exists(in_file):
            print(f"Processing {in_file}...")
            append_x_y_z(in_file)
            print(f"Appended x, y, z values to {in_file}.")
        else:
            print(f"{in_file} does not exist. Skipping.")


if __name__ == "__main__":
    main()
