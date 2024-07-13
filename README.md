# Medical Cost Prediction

This project uses machine learning to predict medical costs based on various patient characteristics. It includes a complete machine learning pipeline for data processing, model training, and a Streamlit web application for easy interaction with the trained model.

## Features

- Predicts medical costs based on age, sex, BMI, number of children, smoking status, and region
- Implements a full machine learning pipeline including data ingestion, transformation, and model training
- Compares multiple regression models (Linear Regression, Lasso, Decision Tree) and selects the best performing one
- Provides a user-friendly web interface for making predictions

## Project Structure

```
MLProject/
│
├── src/
│   └── MLProject/
│       ├── logger.py
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   └── model_trainer.py
│       ├── pipeline/
│       │   ├── predict_pipeline.py
│       │   └── train_pipeline.py
│       ├── utils/
│       │   └── common.py
│       └── config/
│           └── configuration.py
│
├── main.py
├── app.py
├── setup.py
├── requirements.txt
└── README.md
```
## Screenshot from Streamlit App

[![capture-20240713162049250.png](https://i.postimg.cc/G2vjtT6f/capture-20240713162049250.png)](https://postimg.cc/vgHnSTY7)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yusufeneskorkmaz/MLProject.git
   cd MLProject
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -e .
   ```

## Usage

### Training the Model

To run the full training pipeline:

```
python main.py
```

This script will:
- Ingest and preprocess the data
- Transform the data
- Train multiple models and select the best one
- Save the trained model and preprocessor for later use

### Running the Web Application

To start the Streamlit web application:

```
streamlit run app.py
```

This will launch a web interface where you can input patient details and get a prediction for their medical costs.

## File Descriptions

- `main.py`: Script for running the full training pipeline
- `app.py`: Streamlit application for the web interface
- `src/MLProject/components/`: Contains modules for each step of the ML pipeline
- `src/MLProject/pipeline/`: Contains the predict and train pipeline scripts
- `src/MLProject/utils/`: Contains utility functions
- `src/MLProject/config/`: Contains configuration settings

## Dependencies

Main dependencies include:
- pandas
- scikit-learn
- streamlit

See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions to improve the model, extend the functionality, or improve documentation are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).