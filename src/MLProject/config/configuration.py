from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

@dataclass
class ModelEvaluationConfig:
    model_evaluation_file_path = os.path.join("artifacts", "model_evaluation.json")

class ConfigurationManager:
    def __init__(self):
        pass

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = DataIngestionConfig()
        return config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = DataTransformationConfig()
        return config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = ModelTrainerConfig()
        return config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = ModelEvaluationConfig()
        return config