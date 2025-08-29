# File Read & Write Challenge 🖋️

# Read from input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (convert to title case)
modified_content = content.title()

# Write modified content to new file
with open("modified_output.txt", "w") as outfile:
    outfile.write("Modified Text (Title Case):\n\n")
    outfile.write(modified_content)

print("Success! Modified text written to 'modified_output.txt'")


# Error Handling

try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        content = file.read()
    print("\n File Content:\n")
    print(content)

except FileNotFoundError:
    print(" Error: The file does not exist. Please check the name and try again.")

except PermissionError:
    print(" Error: Permission denied. You don’t have access to read this file.")

except Exception as e:
    print(f" An unexpected error occurred: {e}")