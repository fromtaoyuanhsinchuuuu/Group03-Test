import os

def process_blocks():
    """
    Process all block_x_y.txt files in the current directory:
    - Remove the leading zero in the nonce if it starts with 0.
    - Set the nonce value of the last block in each test case to 0.
    """
    # Get all block_x_y.txt files
    block_files = [f for f in os.listdir() if f.startswith('block_') and f.endswith('.txt')]

    # Group files by test case (e.g., block_2_1.txt, block_2_2.txt -> test case 2)
    test_cases = {}
    for block_file in block_files:
        parts = block_file.split('_')
        test_case = parts[1]  # Extract test case number
        if test_case not in test_cases:
            test_cases[test_case] = []
        test_cases[test_case].append(block_file)

    # Process each test case
    for test_case, files in test_cases.items():
        # Sort files by block number (e.g., block_2_1.txt, block_2_2.txt -> sorted)
        files.sort(key=lambda x: int(x.split('_')[2].split('.')[0]))

        # Process each block file in the test case
        for i, block_file in enumerate(files):
            with open(block_file, 'r') as f:
                lines = f.readlines()

            # Extract the nonce line
            nonce_line = lines[-1]
            if nonce_line.startswith("N:"):
                nonce = nonce_line.split(':')[1].strip()

                # Modify nonce if it starts with 0
                if nonce.startswith('0') and len(nonce) > 1:
                    nonce = nonce.lstrip('0')
                    if nonce == '':  # If all digits were 0
                        nonce = '0'

                # Set nonce to 0 for the last block in the test case
                if i == len(files) - 1:
                    nonce = '0'

                # Update the nonce line
                lines[-1] = f"N: {nonce}\n"

            # Write back the modified block file
            with open(block_file, 'w') as f:
                f.writelines(lines)

            print(f"Processed {block_file}: nonce updated.")

if __name__ == "__main__":
    process_blocks()
