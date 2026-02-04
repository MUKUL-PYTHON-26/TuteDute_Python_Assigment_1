# Write text to a new file
user_text = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(user_text + "\n")
file.close()
print("Data successfully written to output.txt.")

# Append more text to the file
additional_text = input("\nEnter additional text to append: ")
file = open("output.txt", "a")
file.write(additional_text + "\n")
file.close()
print("Data successfully appended.")

# Display final content
print("\nFinal content of output.txt:")
file = open("output.txt", "r")
print(file.read())
file.close()