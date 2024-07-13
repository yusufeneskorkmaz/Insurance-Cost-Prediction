import sys
import pandas as pd
from src.MLProject.utils.common import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise Exception(f"Error in prediction: {e}")


class CustomData:
    def __init__(self,
                 age: int,
                 sex: str,
                 bmi: float,
                 children: int,
                 smoker: str,
                 region: str):

        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "age": [self.age],
                "sex": [self.sex],
                "bmi": [self.bmi],
                "children": [self.children],
                "smoker": [self.smoker],
                "region": [self.region],
            }

            def bmi_category(bmi):
                if bmi < 18.5:
                    return 'Underweight'
                elif 18.5 <= bmi < 24.9:
                    return 'Normal weight'
                elif 25 <= bmi < 29.9:
                    return 'Overweight'
                else:
                    return 'Obese'

            df = pd.DataFrame(custom_data_input_dict)
            df['bmi_category'] = df['bmi'].apply(bmi_category)

            return df

        except Exception as e:
            raise Exception(f"Error in creating dataframe: {e}")