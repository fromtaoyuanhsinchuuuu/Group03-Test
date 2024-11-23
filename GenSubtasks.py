import os

def generate_subtasks(input_files, output_file="subtasks.py"):
    """
    Generate a subtasks.py file based on input .in files.
    
    Parameters:
        input_files (list): List of .in file names.
        output_file (str): Output file name for the generated subtasks.py.
    """
    # Fixed parameters
    execution_time = 1  # in seconds
    memory_limit = "64 << 20"  # 64 MB
    output_size_limit = "64 << 20"  # 64 MB

    # Start generating subtasks content
    subtasks = []
    for idx, input_file in enumerate(input_files):
        output_file_name = input_file.replace(".in", ".out")

        # Search for block files related to the input and sort them
        prefix = input_file.replace(".in", "")
        block_files = sorted([f for f in os.listdir() if f.startswith(f"block_{prefix}_")])

        # Generate comparison pairs [['block_i_j.txt', 'ans_i_j.txt'], ...], and sort them
        compare_pairs = [[block_file, block_file.replace("block", "ans")] for block_file in block_files]

        # Append task entry
        subtasks.append(
            f"[{execution_time}, ['{input_file}', '{output_file_name}', 1, {memory_limit}, {output_size_limit}, {block_files}, {compare_pairs}]]"
        )

    # Write to the output Python file
    with open(output_file, "w") as f:
        f.write("[\n")
        f.write(",\n".join(subtasks))
        f.write("\n]\n")

    print(f"Generated {output_file} with {len(input_files)} subtasks.")

if __name__ == "__main__":
    # Gather all .in files in the current directory and sort them
    input_files = sorted([f for f in os.listdir() if f.endswith(".in")])
    
    # Generate the subtasks.py
    generate_subtasks(input_files)
