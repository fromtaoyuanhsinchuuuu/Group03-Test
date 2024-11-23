import os
import random

# Define the data count range for each .in file
DATA_COUNT_CONSTRAINTS = {
    "0.in": (1, 2),
    "1.in": (1, 2),
    "2.in": (2, 5),
    "3.in": (5, 9),
    "4.in": (10, 20),
    "5.in": (21, 24),
    "6.in": (250, 300),
    "7.in": (300, 499),
    "8.in": (1000, 2000),
    "9.in": (4999, 4999)
}

def generate_blocks_for_in_file(in_file):
    """
    Generate block files based on the given .in file.

    Args:
        in_file (str): Path to the .in file.
    """
    with open(in_file, 'r') as file:
        lines = file.readlines()
    
    # Extract n and block file names from the .in file
    n, _ = map(int, lines[0].split())
    block_files = [line.strip() for line in lines[1:n + 1]]
    
    # Determine the number of digits for data (based on n.in filename)
    n_digits = int(in_file.split('.')[0])  # Extract 'n' from 'n.in'
    data_count_range = DATA_COUNT_CONSTRAINTS[in_file]

    prev_hash = 0  # Initialize the previous hash value

    for block_file in block_files:
        k = random.randint(*data_count_range)  # Choose random data count within range
        block_data = generate_block_data(k, n_digits)
        nonce = generate_nonce()

        # Compute hash for the block
        hash_value = compute_hash(block_data, nonce)
        
        # Write block content
        with open(block_file, 'w') as block:
            block.write(f"P: {prev_hash}\n")
            for data in block_data:
                block.write(f"{data}\n")
            block.write(f"N: {nonce}\n")
        
        # Print current block name and its hash value
        print(f"Current Block: {block_file}, Hash Value: {hash_value}")
        
        # Update prev_hash for the next block
        prev_hash = hash_value


def generate_block_data(k, n_digits):
    """
    Generate k pieces of random block data with the specified number of digits.

    Args:
        k (int): Number of data entries.
        n_digits (int): Number of digits for each data entry.

    Returns:
        list: A list of randomly generated data entries.
    """
    data_list = []
    for _ in range(k):
        data = ''.join([str(random.randint(1, 9))] + [str(random.randint(0, 9)) for _ in range(n_digits - 1)])
        data_list.append(data)
    return data_list


def generate_nonce():
    """
    Generate a random nonce value.

    Returns:
        str: A random nonce value.
    """
    return ''.join(random.choices('0123456789', k=8))  # 8-digit nonce


def compute_hash(data_list, nonce):
    """
    Compute the hash value for a block based on its data and nonce.

    Args:
        data_list (list): List of data values.
        nonce (str): Nonce value.

    Returns:
        int: Computed hash value.
    """
    H = 0
    combined_data = data_list + [nonce]  # Combine data and nonce
    for i, di in enumerate(combined_data, start=1):
        di = int(di)
        if i % 25 == 0:
            H = ((H ^ di) << 1) % (2**30)
        else:
            H = (H ^ di) % (2**30)
    return H


def main():
    # Generate blocks for all .in files
    for in_file in [f for f in os.listdir() if f.endswith('.in')]:
        print(f"Processing {in_file}...")
        generate_blocks_for_in_file(in_file)
        print(f"Blocks for {in_file} have been generated.")


if __name__ == "__main__":
    main()
