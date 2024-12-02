# All external imports
from pyspark.sql import SparkSession  ## works only if pyspark is installed. Check "requirements.txt". How to install from requirements.txt file "pip install -r /path/to/requirements.txt"

# All custom imports

# All built in imports
import json

## REQUIREMENTS.txt - How to create:
#1, Once you are done with all packages imports in the virtual env, then just


class InitializeSession:
    def __init__(self, appname):
        self.appname = appname

    def getSparkSession(self):
        # Initialize SparkSession with Delta Lake support
        spark = (
            SparkSession.builder
            .appName(self.appname)
            .getOrCreate()
        )
        return spark


class ReadFilesAndConfig:
    def __init__(self):
        pass

    def fetch_config(self, path_to_config: str) -> dict:
        """ Reads a JSON config file containing paths.
        Args:
            path_to_config (str): The path to the JSON config file.

        Returns:
            dict: A dictionary containing the parsed configuration data.
        """
        with open(path_to_config, "r") as f:
            config_data = json.load(f)
        return config_data

    def readCsv(self, spark: SparkSession, file_type: str, path_to_source: str):
        """ Reads a CSV file into a DataFrame.
        Args:
            path_to_source (str): The path to the CSV file.
            spark (pyspark.sql.SparkSession): A SparkSession instance.

        Returns:
            pyspark.sql.DataFrame: The DataFrame containing the CSV data.
        """
        df_csv = spark.read.format(file_type).option('header', True).load(path_to_source)
        df_csv.show(1)
        return df_csv

    # def old_readCsv(self, spark: SparkSession, raw_file_name, config_dict):
    #     """ Reads a CSV file into a DataFrame based on configuration from a JSON file.
    #     Args:
    #         raw_file_name (str): The name of the file to read (e.g., 'charges', 'damages').
    #         config_dict (dict): The dictionary containing the config data (from fetch_config).

    #     Returns:
    #         pyspark.sql.DataFrame: The DataFrame containing the CSV data.
    #     """
    #     # Extract the file details from the config dictionary using raw_file_name
    #     file_config = config_dict.get('input_files', {}).get(raw_file_name, None)

    #     # file_config = config_dict['input_files'][raw_file_name]

    #     if file_config is None:
    #         raise ValueError(f"File config for '{raw_file_name}' not found in the config.")

    #     file_type = file_config.get('file_type', 'csv')  # Default to 'csv' if not specified
    #     input_file_path = file_config.get('input_file_path', '')

    #     if not input_file_path:
    #         raise ValueError(f"File path for '{raw_file_name}' not found in the config.")

    #     # Call readCsv to read the file
    #     df = self.readCsv(spark, file_type, input_file_path)
    #     return df

