# Case Study: Data Engineering with PySpark
A data engineering project focused on processing and analyzing crash-related datasets using PySpark, with a structured, modular approach.


- [Case Study: Data Engineering with PySpark](#case-study-data-engineering-with-pyspark)
  - [**Project Structure**](#project-structure)
  - [**Directory/Module Details**](#directorymodule-details)
  - [**Features**](#features)
  - [**Prerequisites**](#prerequisites)
  - [**Installation in Local**](#installation-in-local)
    - [Clone the Repository](#1-clone-the-repository)
    - [Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
    - [Install Dependencies](#3-install-dependencies)
  - [**Usage**](#usage)
    - [Run the Solutions Notebook](#1-run-the-solutions-notebook)
    - [Data Initialization](#2-data-initialization)
    - [Modify Analysis Logic](#3-modify-analysis-logic-if-needed)
  - [Contributing](#contributing)
  - [Contact](#contact)



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
- ```env_case_study/``` - 

    A Python virtual environment folder for managing dependencies.
    Excluded from version control via .gitignore.

- ```raw_data/``` - 

    Stores the raw datasets (e.g., Charges_use.csv, Damages_use.csv).
    Used by the modules to load data for processing.
    
- ```config/``` -

    Contains configuration files like json_config.json.
    Defines relative paths for datasets and other settings. This ensures modularity and avoids hardcoding file paths.
    
- ```solutions/``` -

    Contains Python scripts or Jupyter notebooks for executing the data analysis workflows.
    Example: solutions.ipynb includes end-to-end data processing using the modules.

- ```modules/``` -

    Houses custom Python modules:
    setup.py: Initializes the Spark session and provides functions to load datasets dynamically.
    utils.py: Handles reading configurations, file operations, and other utility functions.

## Features
- ```Modular Codebase```: Organized modules for Spark session initialization, configuration management, and file reading.

- ```Dynamic Configuration```: Datasets and file formats are managed via a centralized JSON configuration.

- ```Data Processing``` : PySpark-based processing of large datasets, including filtering, grouping, ranking, and aggregation.

- ```Reusable Components```: Utility functions and classes for commonly performed tasks.


## Prerequisites
- ```Python```: Version 3.8 or higher
- ```PySpark```: Version 3.3.0 or higher
- ```Java Runtime Environment (JRE)```: Version 8 or higher
- ```Additional Tools``` : Git, Jupyter Notebook (optional for running solutions)

## Installation in local

### 1. Clone the Repository:
```
git clone https://github.com/<your-username>/case_study_bcg.git
cd case_study_bcg
```

### 2. Set Up a Virtual Environment:

```
python -m venv env_case_study
source env_case_study/bin/activate  # For Unix-based systems
env_case_study\Scripts\activate     # For Windows
```

### 3. Install Dependencies:

```
pip install -r requirements.txt
```

## Usage

### 1. Run the Solutions Notebook:

Navigate to the solutions directory and execute the Jupyter notebook.

- 1.1 Either run the notebook manually, 
OR (use below cmd command),

```
cd solutions
jupyter notebook solutions.ipynb
```

### 2. Data Initialization:

- The project is configured to automatically load the datasets and process them based on the paths specified in config/json_config.json. No manual data-loading steps are required.

### 3. Modify Analysis Logic (if needed):

To extend or customize the analysis, edit the solutions.ipynb notebook or create a new script in the solutions/ directory using the pre-built modules in modules/.


This streamlined section communicates that everything is pre-configured and ready to go without requiring the user to deal with intermediate steps like data loading. It emphasizes usability and modularity, aligning with your project goals.

## Example Config (config/json_config.json)

``` 

{
  "input_files": {
    "charges": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Charges_use.csv"
    },
    "damages": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Damages_use.csv"
    },
    "endorse_use": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Endorse_use.csv"
    },
    "primary_person_use": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Primary_Person_use.csv"
    },
    "restrict_use": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Restrict_use.csv"
    },
    "units_use": {
      "file_type": "csv",
      "input_file_path": "../raw_data/Units_use.csv"
    }
  }
}

```

## Contributing
  -  Fork the Repository.
  - Create a Branch
  ```
  git checkout -b feature-name
```
- Commit your changes
```
git commit -m "Description of changes"
```
- Push to the Branch:
```
git push origin feature-name
```
- Open a pull request 


## Contact
- For any questions or feedback, feel free to reach out: ankittabu@gmail.com

