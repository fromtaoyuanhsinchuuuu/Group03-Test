#!/bin/bash

# Iterate through all .in files in the current directory
for input_file in *.in; do
    # Derive the output file name
    output_file="${input_file%.in}.out"
    
    # Execute the program with the input file and redirect the output
    ./a.out < "$input_file" > "$output_file"
    
    # Display a message indicating the result
    echo "Processed $input_file -> $output_file"
done

