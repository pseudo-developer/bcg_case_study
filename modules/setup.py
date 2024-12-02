import os, sys
from modules.utils import InitializeSession, ReadFilesAndConfig


class DataReader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.read_files_and_config = ReadFilesAndConfig()
        self.spark = None
        self.config_dict = None

    def initialize_spark_session(self, app_name: str = "MyApp"):
        """Initializes and returns a Spark session."""
        try:
            session = InitializeSession(app_name)
            self.spark = session.getSparkSession()
            print("Spark version is:", self.spark.version)
        except Exception as e:
            print("An error occurred while initializing Spark:", e)
            raise

    def load_config(self):
        """Loads the configuration from the JSON config file."""
        try:
            self.config_dict = self.read_files_and_config.fetch_config(self.config_path)
            print("\n------ Printing config below ------")
            print(self.config_dict)
            print("------ Config ends ------", '\n')
        except Exception as e:
            print("An error occurred while loading config:", e)
            raise

    def read_data(self, dataset_name: str):
        """Reads a dataset based on its name using the configuration."""
        try:
            dataset_config = self.config_dict['input_files'][dataset_name]
            file_type = dataset_config['file_type']
            file_path = dataset_config['input_file_path']
            return self.read_files_and_config.readCsv(self.spark, file_type, file_path)
        except Exception as e:
            print(f"An error occurred while reading dataset {dataset_name}:", e)
            raise

    def read_all_datasets(self):
        """Reads all datasets listed in the configuration."""
        datasets = {}
        try:
            for dataset_name in self.config_dict['input_files']:
                print(f"Reading dataset: {dataset_name}:")
                datasets[dataset_name] = self.read_data(dataset_name)
                print('\n')
        except Exception as e:
            print("An error occurred while reading all datasets:", e)
            raise
        return datasets


def read_all_data():
    """Main function to initialize and read all datasets."""
    config_path = '../config/json_config.json'  # Replace with your config file path
    data_reader = DataReader(config_path)

    # Initialize Spark and load configuration
    data_reader.initialize_spark_session()
    data_reader.load_config()

    # Read all datasets
    datasets = data_reader.read_all_datasets()

    # Unpack and return the datasets
    return (
        datasets.get('charges'),
        datasets.get('damages'),
        datasets.get('endorse_use'),
        datasets.get('primary_person_use'),
        datasets.get('restrict_use'),
        datasets.get('units_use'),
    )
