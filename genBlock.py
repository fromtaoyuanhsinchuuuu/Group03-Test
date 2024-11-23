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
    H = 0
    for i, value in enumerate(data_list + [nonce], start=1):
        if i % 25 == 0:
            H = ((H ^ value) << 1) % (2 ** 30)
        else:
            H = (H ^ value) % (2 ** 30)
    return H


def generate_blocks(in_file, block_data_width):
    """
    Generate block files based on the given .in file and data width.

    Args:
        in_file (str): The name of the .in file.
        block_data_width (int): The width of the data values (in digits).
    """
    # Read the .in file to get the number of blocks (n)
    with open(in_file, 'r') as file:
        lines = file.readlines()

    n, _ = map(int, lines[0].split())
    block_files = [line.strip() for line in lines[1:n + 1]]

    prev_hash = 0  # Initial previous hash

    for i, block_file in enumerate(block_files):
        # Determine the number of data entries for this block based on the .in file rules
        if in_file.startswith("0.in"):
            k_range = (1, 2)
        elif in_file.startswith("1.in"):
            k_range = (2, 2)
        elif in_file.startswith("2.in"):
            k_range = (2, 5)
        elif in_file.startswith("3.in"):
            k_range = (5, 9)
        elif in_file.startswith("4.in"):
            k_range = (10, 20)
        elif in_file.startswith("5.in"):
            k_range = (21, 24)
        elif in_file.startswith("6.in"):
            k_range = (250, 300)
        elif in_file.startswith("7.in"):
            k_range = (300, 499)
        elif in_file.startswith("8.in"):
            k_range = (1000, 2000)
        elif in_file.startswith("9.in"):
            k_range = (4999, 4999)
        else:
            raise ValueError("Unsupported .in file")

        k = random.randint(*k_range)

        # Generate k data entries of the specified width
        data_list = [int("".join(random.choices("0123456789", k=block_data_width))) for _ in range(k)]

        # Determine the nonce to keep the hash consistent with the next block
        nonce = random.randint(0, 2 ** 30 - 1)
        hash_value = calculate_hash(data_list, nonce)

        # Write the block file
        with open(block_file, 'w') as file:
            file.write(f"P: {prev_hash}\n")
            for idx, data in enumerate(data_list, start=1):
                file.write(f"{idx}: {data}\n")
            file.write(f"N: {nonce}\n")

        # Update the previous hash for the next block
        prev_hash = hash_value


def main():
    # Mapping of .in files to data widths
    data_widths = {
        "0.in": 1,
        "1.in": 2,
        "2.in": 2,
        "3.in": 3,
        "4.in": 4,
        "5.in": 5,
        "6.in": 6,
        "7.in": 7,
        "8.in": 8,
        "9.in": 9,
    }

    for in_file, data_width in data_widths.items():
        print(f"Generating blocks for {in_file} with data width {data_width}...")
        generate_blocks(in_file, data_width)
        print(f"Blocks for {in_file} generated.")


if __name__ == "__main__":
    main()
