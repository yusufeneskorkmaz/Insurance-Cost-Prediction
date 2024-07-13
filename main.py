from src.MLProject.pipeline.train_pipeline import start_training_pipeline
from src.MLProject.logger import logger

if __name__ == "__main__":
    try:
        logger.info("Starting the training pipeline")
        start_training_pipeline()
        logger.info("Training pipeline completed successfully")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e