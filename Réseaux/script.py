import os

# Go in each folder and create a file named "Readme.md" with the content "This is the README file for [folder name]"
for folder in os.listdir():
    if os.path.isdir(folder):
        with open(os.path.join(folder, "Readme.md"), "w") as f:
            f.write(f"This is the README file for {folder}")