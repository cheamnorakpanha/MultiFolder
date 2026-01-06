import os

# Set the range of folder numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop through and create folders
for i in range(start, end + 1):
    folder_name = f"RE-{i}-2026"
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")
        # print("Total folders created so far:", i - start + 1)
    except Exception as e:
        print(f"Failed to create {folder_name}: {e}")

# We use i - start + 1 to count the total folders created
print("======================================")
print("  => Total folders created so far:", i - start + 1)
print("======================================")