try:
    # Opening the file to read
    file = open("sample.txt", "r")

    print("Reading file content:")
    # Printing content line by line
    for line in file:
        print(line.strip())

    file.close()

except FileNotFoundError:
    # Error message if file is missing
    print("Error: The file 'sample.txt' was not found.")