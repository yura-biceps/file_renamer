from pathlib import Path
import datetime
import shutil


def main():
    source_folder = Path('./test_files')
    destination_folder = Path('./formatted_files')
    files = [f.name for f in source_folder.iterdir() if f.is_file()]
    print("Files in the source folder: ")
    print(files)
    custom_tag = input("Specify tag for files: ") # check if the folder exists
    destination_folder.mkdir(parents=True, exist_ok=True)
    for file in files:
        new_name = f"{datetime.date.today()}_{custom_tag}_{file}"
        new_name = new_name.replace(' ', '_') # replace spaces with underscores 
        source_file = source_folder / file
        formatted_file = destination_folder / new_name
        print(f"Renaming and moving {source_file} to {formatted_file}")
        shutil.copyfile(source_file, formatted_file)


if __name__ == "__main__":
    main()
