import os
import shutil

def main():
    osu_directory = input("Please input your osu! directory: ")
    desired_bg_directory = input("Please input the directory of the image you want to replace the osu! background with: ")

    confirmation = input("Are you sure you want to replace every PNG or JPG file in your osu! songs folder with the background of your choice? (Type \"YES I DO\"): ")

    if confirmation == "YES I DO":
        # Extract the file extension of the desired background image
        _, bg_extension = os.path.splitext(desired_bg_directory)
        bg_extension = bg_extension.lower()

        for root, _, files in os.walk(osu_directory):
            for file in files:
                # Check if the file is a PNG or JPG image
                if file.lower().endswith('.png') or file.lower().endswith('.jpg'):
                    try:
                        # Get the original file path
                        original_file_path = os.path.join(root, file)
                        print(original_file_path)
                        # Remove the existing file if it exists
                        os.remove(original_file_path)
                        
                        # Copy the desired background and rename it
                        shutil.copy(desired_bg_directory, original_file_path)
                        
                        # Rename the copied background image to its original filename with the same extension
                        new_file_path = os.path.splitext(original_file_path)[0] + os.path.splitext(file)[1]
                        os.rename(original_file_path, new_file_path)
                    except FileNotFoundError:
                        print("Error: File not found.")
                        exit()
                    except shutil.SameFileError:
                        print("Error: Cannot replace the background with the same image.")
                        exit()

        print("PNG or JPG files replaced successfully!")
    else:
        print("Operation aborted.")

if __name__ == "__main__":
    main()