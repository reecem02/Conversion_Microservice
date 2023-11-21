def conversion(filename):
    try:
        # Open the file in read and write mode ('r+')
        with open(filename, 'r+') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Extract numbers from a single line and convert to float
            # replace commas with periods, use strip to remove extra white spaces, and split by space
            num1, num2 = map(lambda x: float(x.replace(',', '.')), lines[0].strip().split())
            # print("Number 1:", num1)
            # print("Number 2:", num2)

            # Perform conversion
            result = num1 * num2

            # Move the file cursor to the beginning
            file.seek(0)
            
            # Write the result back to the file
            file.write(str(result))
            # print("Conversion result:", result)
    except Exception as e:
        # Print an error message with exception details
        print(f"Error: {e}")

# Example usage
input_output_file = 'input.txt'
conversion(input_output_file)
