# Open a file
file = open("example.txt", "w")

# Write to the file
file.write("Hello World!")

# Close the file
file.close()

# Open the file again
file = open("example.txt", "r")

# Read the contents of the file
contents = file.read()

# Print the contents of the file
print(contents)

# Close the file
file.close()
