import os

# String inputs
start = input("Enter the starting number: ")
end = input("Enter the ending number: ")

# Convert to int only for looping
start_int = int(start)
end_int = int(end)

# Get length for zero-padding (e.g. 001)
width = len(start)

for i in range(start_int, end_int + 1):
    folder_name = str(i).zfill(width)
    folder_name = f"IMP-{folder_name}"

    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created folder: {folder_name}")
    except Exception as e:
        print(f"Error creating folder {folder_name}: {e}")

print("======================================")
print("  => Total folders created so far:", end_int - start_int + 1)
print("======================================")