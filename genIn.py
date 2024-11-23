import random
import os

def generate_in_and_blocks(file_name, n, q, k_range, block_prefix):
    """
    Generate .in file and corresponding block files with the given parameters.
    """
    # Generate .in file
    with open(file_name, 'w') as in_file:
        in_file.write(f"{n} {q}\n")
        block_files = []

        for i in range(1, n + 1):
            block_file = f"{block_prefix}_{i}.txt"
            block_files.append(block_file)
            in_file.write(f"{block_file}\n")

            # Generate block content
            generate_block(block_file, random.randint(*k_range))

def generate_block(block_file, k):
    """
    Generate a block file with given k data entries.
    """
    with open(block_file, 'w') as block:
        block.write("P: 0\n")
        for i in range(1, k + 1):
            data = random.randint(1, 2**30 - 1)
            block.write(f"{i}: {data}\n")
        block.write("N: 0\n")

# Parameters for each .in file
configs = {
    "2.in": (5, 5, (2, 5)),
    "3.in": (10, 10, (5, 9)),
    "4.in": (12, 20, (10, 20)),
    "5.in": (14, 25, (21, 24)),
    "6.in": (16, 500, (250, 300)),
    "7.in": (18, 1000, (300, 499)),
    "8.in": (20, 1000, (1000, 2000)),
    "9.in": (20, 1000, (4999, 4999))
}

# Generate .in files and their corresponding blocks
for in_file, (n, q, k_range) in configs.items():
    generate_in_and_blocks(in_file, n, q, k_range, in_file.split(".")[0])

# List generated files
os.listdir()
