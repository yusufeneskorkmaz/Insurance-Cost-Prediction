import streamlit as st
import pandas as pd
from src.MLProject.pipeline.predict_pipeline import CustomData, PredictPipeline


def main():
    st.title('Medical Cost Prediction')

    # User input
    age = st.number_input('Age', min_value=0, max_value=100, value=25)
    sex = st.selectbox('Sex', ['male', 'female'])
    height = st.number_input('Height (cm)', min_value=50, max_value=250, value=170)
    weight = st.number_input('Weight (kg)', min_value=10, max_value=200, value=70)
    children = st.number_input('Number of Children', min_value=0, max_value=10, value=0)
    smoker = st.selectbox('Smoker', ['yes', 'no'])
    region = st.selectbox('Region', ['northeast', 'northwest', 'southeast', 'southwest'])

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)

    # Prediction button
    if st.button('Predict'):
        data = CustomData(
            age=age,
            sex=sex,
            bmi=bmi,
            children=children,
            smoker=smoker,
            region=region
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        st.write(f'The predicted medical cost is: ${results[0]:.2f}')
        st.write(f'Calculated BMI is: {bmi:.2f}')


if __name__ == '__main__':
    main()