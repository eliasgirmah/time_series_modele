# Stock Price Forecasting using ARIMA

This project aims to forecast  stock prices using an ARIMA (AutoRegressive Integrated Moving Average) model. The model is trained on historical stock price data and evaluated against actual prices to assess its effectiveness in handling highly volatile financial data.

## Table of Contents
- [Project Structure](#project-structure)
- [Workflow](#workflow)
  - [Data Collection & Preprocessing](#data-collection--preprocessing)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Modeling with ARIMA](#modeling-with-arima)
  - [Evaluation & Results](#evaluation--results)
- [Key Files](#key-files)
- [Installation](#installation)
- [Usage](#usage)
  - [Preprocess Data](#preprocess-data)
  - [Train ARIMA Model](#train-arima-model)
  - [View Results](#view-results)
- [Interpretation of Model Output](#interpretation-of-model-output)


## Workflow

### Data Collection & Preprocessing
1. **Collect stock price data**: Obtain historical stock price data for training and testing.
2. **Data Cleaning**: Handle missing values, split data into training and testing sets, and scale if necessary.

### Exploratory Data Analysis (EDA)
1. **Trend Analysis**: Examine stock trends, seasonality, and volatility to understand historical performance.
2. **Visualization**: Generate visualizations to support model selection and parameter tuning.

### Modeling with ARIMA
1. **Model Training**: Train the ARIMA model on the training data.
2. **Parameter Tuning**: Optimize parameters through techniques like grid search.
3. **Forecasting**: Forecast stock prices for the test period.

### Evaluation & Results
1. **Metrics**: Use evaluation metrics like Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) to assess model accuracy.
2. **Visualization**: Plot the forecast versus actual data, highlighting model performance and limitations.

## Key Files

- `notebooks/EDA.ipynb`: Jupyter notebook for data exploration and visualization.
- `notebooks/ARIMA_Modeling.ipynb`: Jupyter notebook for ARIMA model training and forecasting.
- `src/data_processing.py`: Script for data preprocessing.
- `src/modeling.py`: Script for training and forecasting with the ARIMA model.
- `output/forecast_plot.png`: Plot comparing actual vs. forecasted prices.

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/eliasgirmah/time_series_modele.git
cd time_series_modele
pip install -r requirements.txt


