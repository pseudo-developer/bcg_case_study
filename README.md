# Case Study: Data Engineering with PySpark
A data engineering project focused on processing and analyzing crash-related datasets using PySpark, with a structured, modular approach.


## Project Structure
The project is organized into the following directories and files to ensure clarity and modularity:
```
case_study_bcg/
├── env_case_study/       # Virtual environment for package management (ignored by Git)
├── raw_data/             # Contains raw input files (CSV files)
├── config/               # Configuration files
│   └── json_config.json  # Stores relative paths and settings for datasets
├── solutions/            # Contains Jupyter notebooks or Python scripts for data processing and analysis
│   └── solutions.ipynb   # Main notebook or script to run analysis
├── modules/              # Custom Python modules
│   ├── setup.py          # Handles Spark session setup and data loading from raw files
│   ├── utils.py          # Utility functions for reading config files and reusable operations
├── .gitignore            # Specifies files and directories to be ignored by Git
├── README.md             # Documentation file (this file)
```


## Directory/Module Details
```env_case_study/```

A Python virtual environment folder for managing dependencies.
Excluded from version control via .gitignore.
raw_data/

Stores the raw datasets (e.g., Charges_use.csv, Damages_use.csv).
Used by the modules to load data for processing.
config/

Contains configuration files like json_config.json.
Defines relative paths for datasets and other settings. This ensures modularity and avoids hardcoding file paths.
solutions/

Contains Python scripts or Jupyter notebooks for executing the data analysis workflows.
Example: solutions.ipynb includes end-to-end data processing using the modules.
modules/

Houses custom Python modules:
setup.py: Initializes the Spark session and provides functions to load datasets dynamically.
utils.py: Handles reading configurations, file operations, and other utility functions.
