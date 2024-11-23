import random
import os

def calculate_hash(data_list, nonce):
    """
    Calculate the hash value for a block using the given data and nonce.

    Args:
        data_list (list): A list of data values (integers).
        nonce (int): The nonce value.

    Returns:
        int: The calculated hash value.
    """
    hash_value = 0
    for idx, value in enumerate(data_list + [nonce], start=1):
        if idx % 25 == 0:
            hash_value = ((hash_value ^ value) << 1) % (2**30)
        else:
            hash_value = (hash_value ^ value) % (2**30)
    return hash_value


def generate_in_and_blocks(in_file, n, q, k_range, data_digits):
    """
    Generate an .in file and the corresponding block files.

    Args:
        in_file (str): Name of the .in file to generate.
        n (int): Number of blocks.
        q (int): Number of commands.
        k_range (tuple): Range of data lines per block (min, max).
        data_digits (int): Number of digits for each data value.
    """
    block_files = [f"block_{in_file.split('.')[0]}_{i}.txt" for i in range(1, n + 1)]
    
    # Write the .in file
    with open(in_file, 'w') as file:
        file.write(f"{n} {q}\n")
        file.writelines(f"{block_file}\n" for block_file in block_files)
    
    # Generate corresponding block files
    prev_hash = 0  # Initial prev_hash for the first block
    for block_file in block_files:
        # Generate random number of data lines within the range
        num_data_lines = random.randint(k_range[0], k_range[1])
        data_list = [random.randint(10**(data_digits-1), 10**data_digits - 1) for _ in range(num_data_lines)]

        # Random nonce generation
        nonce = random.randint(10**(data_digits-1), 10**data_digits - 1)

        # Write the block file
        with open(block_file, 'w') as block:
            block.write(f"P: {prev_hash}\n")
            for idx, data in enumerate(data_list, start=1):
                block.write(f"{idx}: {data}\n")
            block.write(f"N: {nonce}\n")
        
        # Update prev_hash for the next block
        prev_hash = calculate_hash(data_list, nonce)


def main():
    # Define the (n, q, k) constraints for each .in file
    configs = [
        (2, 1, (1, 2), 1),       # 0.in: n=2, q=1, k=(1~2), data digits=1
        (2, 1, (2, 2), 2),       # 1.in: n=2, q=1, k=2, data digits=2
        (5, 5, (2, 5), 2),       # 2.in: n=5, q=5, k=(2~5), data digits=2
        (10, 10, (5, 9), 3),     # 3.in: n=10, q=10, k=(5~9), data digits=3
        (12, 20, (10, 20), 3),   # 4.in: n=12, q=20, k=(10~20), data digits=3
        (14, 25, (21, 24), 4),   # 5.in: n=14, q=25, k=(21~24), data digits=4
        (16, 500, (250, 300), 4),# 6.in: n=16, q=500, k=(250~300), data digits=4
        (18, 1000, (300, 499), 5), # 7.in: n=18, q=1000, k=(300~499), data digits=5
        (20, 1000, (1000, 2000), 5), # 8.in: n=20, q=1000, k=(1000~2000), data digits=5
        (20, 1000, (4999, 4999), 6)  # 9.in: n=20, q=1000, k=4999, data digits=6
    ]
    
    # Generate each .in file and corresponding block files
    for i, (n, q, k_range, data_digits) in enumerate(configs):
        in_file = f"{i}.in"
        print(f"Generating {in_file}...")
        generate_in_and_blocks(in_file, n, q, k_range, data_digits)
        print(f"{in_file} and corresponding blocks generated successfully.")


if __name__ == "__main__":
    main()
