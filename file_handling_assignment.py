# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers\n")
        print("File created and initial content written successfully.")
except Exception as e:
    print(f"Error occurred while creating the file: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Content of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied to open the file.")
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
        print("Content appended to my_file.txt.")
except Exception as e:
    print(f"Error occurred while appending to the file: {e}")
finally:
    print("Execution completed.")

