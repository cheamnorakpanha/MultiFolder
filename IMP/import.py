import os

# Set the range of folder numbers
start = 279
end = 286

# Loop through and create folders
for i in range(start, end + 1):
    folder_name = f"IMP-{i}"
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")
    except Exception as e:
        print(f"Failed to create {folder_name}: {e}")