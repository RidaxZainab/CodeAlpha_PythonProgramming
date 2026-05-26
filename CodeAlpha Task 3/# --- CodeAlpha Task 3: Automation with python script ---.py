import os
import shutil

source_folder = "my_images"
destination_folder = "moved_images"

if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"Created '{source_folder}' folder. Please add some .jpg files in it and run again.")

else:
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    all_files = os.listdir(source_folder)
    moved_count = 0

    for file_name in all_files:
        if file_name.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            
            shutil.move(source_path, destination_path)
            print(f"Moved: {file_name}")
            moved_count += 1

    print("-----------------------------------------")
    print(f"Automation complete! Total .jpg files moved: {moved_count}")