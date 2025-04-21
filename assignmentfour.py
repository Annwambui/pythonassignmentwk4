def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()  # Read the content of the file

        # Modify the content (we are converting all text to uppercase)
        modified_content = content.upper()  # Modify content (example: convert to uppercase)

        # Write the modified content to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File has been successfully read from {input_filename} and modified content written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read/write to {input_filename} or {output_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Prompt user for the filename
input_filename = input("Enter the name of the input file: ")
output_filename = input("Enter the name of the output file: ")

# Call the function with user input
read_and_modify_file(input_filename, output_filename)
