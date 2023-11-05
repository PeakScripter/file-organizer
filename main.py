import os
import shutil

source_directory = '/path/to/source_directory'  # Replace with your source directory
destination_directory = '/path/to/destination_directory'  # Replace with your destination directory

file_extensions = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.jpeg': 'Images',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.txt': 'Documents',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mp3': 'Audio',
}

for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        folder_name = file_extensions.get(file_extension, 'Other')
        destination_folder = os.path.join(destination_directory, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        shutil.move(file_path, os.path.join(destination_folder, filename))

print("File organizing complete.")
