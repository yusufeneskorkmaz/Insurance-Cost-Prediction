import os
import sys

from dataclasses import dataclass
from src.MLProject.logger import logger
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

from src.MLProject.utils.common import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logger.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Decision Tree": DecisionTreeRegressor(),
            }
            params = {
                "Linear Regression": {},
                "Lasso": {
                    'alpha': [0.1, 0.5, 1],
                    'selection': ['random', 'cyclic']
                },
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse'],
                    'splitter': ['best', 'random']
                }
            }

            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                                 models=models, param=params)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise Exception("No best model found")
            logger.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            mae = mean_absolute_error(y_test, predicted)
            mse = mean_squared_error(y_test, predicted)
            r2 = r2_score(y_test, predicted)
            return mae, mse, r2


        except Exception as e:
            raise Exception(f"Error in initiate_model_trainer: {e}")