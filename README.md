# Medical Cost Prediction Model

This repository contains a machine learning project focused on predicting medical insurance costs based on various inputs such as age, BMI, smoking status, and region. The goal is to build and deploy a model that can accurately estimate the insurance premium for an individual given their characteristics.

Streamlit link - https://medicalcostpredictionmodel.streamlit.app/

Built and fine-tuned by [Satyam Bhagat](https://github.com/satyam2006-cmd).


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Medical costs can vary significantly based on demographic and lifestyle factors. By leveraging machine learning, this project aims to help insurance companies and individuals estimate costs with greater accuracy and transparency.

## Features

- Data preprocessing and visualization
- Machine learning model training (Linear Regression, Decision Tree, Random Forest, etc.)
- Model evaluation and comparison
- Prediction interface for new data
- (Optional) Deployment via web app (e.g., Flask, Streamlit)

## Dataset

The dataset used is typically the [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle, which contains the following columns:
- `age`: Age of the primary beneficiary
- `sex`: Gender of the beneficiary
- `bmi`: Body Mass Index (numeric value)
- `children`: Number of dependents
- `smoker`: Whether the beneficiary is a smoker
- `region`: Residential area in the US
- `charges`: Medical insurance cost (target variable)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/satyam2006-cmd/Medical-Cost-Prediction-Model-.git
   cd Medical-Cost-Prediction-Model-
   ```

2. Install dependencies (recommended: use a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To train the model and generate predictions:

1. Ensure the dataset (e.g., `insurance.csv`) is placed in the project directory.
2. Run the main script:
   ```bash
   python main.py
   ```
   *(Adjust script name as needed based on your project structure.)*

3. For web-based deployment, run:
   ```bash
   streamlit run app.py
   ```
   *(If a Streamlit or Flask app is included.)*

## Model

The project explores multiple regression algorithms including:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- (Optional) XGBoost, etc.

Model performance is evaluated using metrics like RMSE, MAE, and R².

## Results

Sample results and analysis are included in the `notebooks/` or `reports/` directory. Key findings:
- [Highlight best model performance]
- [Include sample prediction plot or table]

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

---

**Author:** [satyam2006-cmd](https://github.com/satyam2006-cmd)
