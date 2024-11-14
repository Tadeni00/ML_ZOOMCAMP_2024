# import os
# from pathlib import Path
# import logging

# # Setting up logging configuration
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# def create_project_structure(base_dir: str, file_structure: list):
#     """
#     Creates the project directory structure based on a given file list.

#     Parameters:
#         base_dir (str): The base directory where the structure will be created.
#         file_structure (list): A list of file paths to create within the base directory.
#     """
#     for filepath in file_structure:
#         # Construct full path
#         full_path = Path(base_dir) / filepath
#         directory, filename = os.path.split(full_path)

#         # Create directory if it does not exist
#         if directory:
#             os.makedirs(directory, exist_ok=True)
#             logging.info(f"Directory created: {directory} for file: {filename}")

#         # Create the file if it doesn't exist or is empty
#         if not full_path.exists() or full_path.stat().st_size == 0:
#             with open(full_path, "w") as f:
#                 pass  # Create an empty file
#             logging.info(f"Empty file created: {full_path}")
#         else:
#             logging.info(f"File already exists and is not empty: {filename}")

# # Define the project structure
# project_structure = [
#     "data/customers_data.csv",
#     "notebooks/EDA.ipynb",
#     "src/data_ingestion.py",
#     "src/data_preprocessing.py",
#     "src/feature_engineering.py",
#     "src/data_transformation.py",
#     "src/clustering.py",
#     "src/utils.py",
#     "artifacts/df_cleaned.csv",
#     "artifacts/df_scaled.csv",
#     "artifacts/df_segmented.csv",
#     "main.py",
#     "requirements.txt"
# ]

# # Set the base directory (modify as needed)
# base_dir = "project"

# # Invoke the function to create the project structure
# if __name__ == "__main__":
#     create_project_structure(base_dir, project_structure)

import os

# Define the main project directory
project_name = "click_through"

# Define the folder structure
structure = {
    "data": ["customers_data.csv"],
    "notebooks": ["EDA.ipynb"],
    "src": [
        "data_ingestion.py",
        "data_preprocessing.py",
        "feature_engineering.py",
        "data_transformation.py",
        "clustering.py",
        "utils.py",
    ],
    "artifacts": [],
    "templates": ["home.html"],
    "logs": ["app.log"],
    "": ["app.py", "docker-compose.yaml", "Dockerfile", "README.md", "requirements.txt"],
}

# Create the directories and files
for folder, files in structure.items():
    # Create the folder path
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)

    # Create each file in the current folder
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as f:
            # Adding a placeholder comment to each file for initialization
            f.write(f"# Placeholder for {file_name}\n")

print(f"Project structure for '{project_name}' has been created successfully!")
