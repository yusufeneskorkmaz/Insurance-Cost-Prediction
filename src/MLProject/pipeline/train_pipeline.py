import os
import sys
from src.MLProject.logger import logging
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_transformation import DataTransformation
from src.MLProject.components.model_trainer import ModelTrainer

def start_training_pipeline():
    try:
        logging.info("Starting the training pipeline")

        # Data Ingestion
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

        # Model Training
        model_trainer = ModelTrainer()
        mae, mse, r2 = model_trainer.initiate_model_trainer(train_arr, test_arr)

        logging.info(f"Training completed. Model performance: MAE={mae}, MSE={mse}, R2={r2}")

    except Exception as e:
        logging.error(f"An error occurred in the training pipeline: {e}")
        raise e

if __name__ == "__main__":
    start_training_pipeline()