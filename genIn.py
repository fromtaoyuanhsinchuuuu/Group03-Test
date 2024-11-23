import os

def generate_in_file(file_name, n, q, block_prefix):
    """
    Generate .in file with the given parameters, but do not create block files.
    """
    # Generate .in file
    with open(file_name, 'w') as in_file:
        in_file.write(f"{n} {q}\n")

        # Write block file names based on the format block_n_i.txt
        for i in range(1, n + 1):
            block_file = f"block_{file_name.split('.')[0]}_{i}.txt"
            in_file.write(f"{block_file}\n")


# Parameters for each .in file
configs = {
    "0.in": (2, 1),
    "1.in": (2, 1),
    "2.in": (5, 5),
    "3.in": (10, 10),
    "4.in": (12, 20),
    "5.in": (14, 25),
    "6.in": (16, 500),
    "7.in": (18, 1000),
    "8.in": (20, 1000),
    "9.in": (20, 1000)
}

# Generate .in files with only block references
for in_file, (n, q) in configs.items():
    generate_in_file(in_file, n, q, in_file.split(".")[0])

# List generated .in files
print("Generated .in files:")
print([f for f in os.listdir() if f.endswith('.in')])
