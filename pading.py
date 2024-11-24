# this code pading 0 to the number at the last line of certain file to EXACTLY 10 digits

import os
import re

# Iterate through all files in the current directory
for filename in os.listdir("."):
    if filename.startswith("ans") and filename.endswith(".txt"):
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Find the last line starting with 'N:'
        if lines and lines[-1].startswith("N:"):
            last_line = lines[-1]
            match = re.match(r"N:\s*(\d+)", last_line)
            if match:
                # Extract the number and pad it with leading zeros to 10 digits
                number = match.group(1)
                padded_number = number.zfill(10)
                # Update the last line
                lines[-1] = f"N: {padded_number}\n"

                # Write the modified content back to the file
                with open(filename, "w") as file:
                    file.writelines(lines)
                print(f"Modified {filename}: N is now {padded_number}")
        else:
            print(f"No valid 'N:' line found in {filename}")
