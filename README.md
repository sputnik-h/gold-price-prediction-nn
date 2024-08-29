# Gold Forecast: Predicting Gold Price Trends Using Neural Networks

This project aims to predict the daily changes in gold prices using a deep learning model. By examining key financial indicators such as the S&P 500, Consumer Price Index, and other precious metals, we provide a tool for investors and financial experts to make informed decisions about future gold prices. The project includes an interactive web application that allows users to input data and receive predictions in real-time, fully deployed on Google Cloud for accessibility and scalability.

## Table of Contents
- [Introduction](#introduction)
- [Data Collection and Preparation](#data-collection-and-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Hyperparameter Optimization](#hyperparameter-optimization)
- [Front-End Application](#front-end-application)
- [Conclusion](#conclusion)
- [Contributors](#contributors)

## Introduction

In the investment world, gold is a critical asset class, often seen as a hedge against market volatility. Gold prices are influenced by various factors, including the S&P 500 index, inflation indices from the US and EU, and prices of other precious metals like silver and platinum. This project uses time series analysis and neural network models to predict gold price trends, providing valuable insights for investors.

## Data Collection and Preparation

[The dataset](https://www.kaggle.com/datasets/sid321axn/gold-price-prediction-dataset) used in this project contains 1,718 observations, including daily prices of gold, trading volumes, and various financial indicators such as:
- S&P 500 Index
- US Dollar Index (USDI)
- Consumer Price Indexes for US and EU
- Prices of other commodities like silver and oil

### Data Preparation Steps:
1. **Data Cleaning**: Handled missing values and filtered out irrelevant data.
2. **Feature Engineering**: Created categorical features indicating daily changes and added lag variables to capture temporal dependencies.
3. **Normalization**: Applied MinMaxScaler to standardize the data, ensuring all features contribute equally to the model.

## Exploratory Data Analysis (EDA)

EDA revealed strong correlations between gold prices and several key indicators, justifying the predictive modeling approach. Key visualizations include:
- **Time Series Plots**: Showed historical trends in gold prices.
- **Correlation Heatmap**: Highlighted relationships between financial indicators and gold price movements.

## Model Architecture

The neural network model was built using Keras and optimized through various configurations:
- **Baseline Model**: Consists of two hidden layers (8 and 4 neurons) with ReLU activation, using the Adam optimizer. Achieved a test accuracy of 74.7%.
- **Improved Model**: Further optimized with additional layers, nodes, and epochs, achieving a test accuracy of 78.9%.

### Model Summary:
- **Input Layer**: Accepts time series features and engineered variables.
- **Hidden Layers**: Multiple layers with ReLU activation functions.
- **Output Layer**: Sigmoid function to predict price movement (increase or decrease).
- **Optimizer**: Adam with various learning rates tuned for best performance.

## Results

The model performed well in predicting daily trends of gold prices, with accuracy rates reaching up to 78.9% after hyperparameter tuning. The results suggest that gold prices are relatively stable, with identifiable patterns driven by macroeconomic factors and other precious metals.

## Hyperparameter Optimization

We used Keras Tuner for hyperparameter optimization, experimenting with:
- Number of units in each layer.
- Learning rates.
- Number of epochs.

### Optimal Configuration:
- **First Layer Units**: 26
- **Learning Rate**: 0.01
- **Best Validation Accuracy**: 73.45%

## Front-End Application

An interactive web application was built to make the model accessible to non-technical users. The application features:
- **HTML Front End**: User-friendly interface for inputting data and viewing predictions.
- **Python Backend**: Processes user inputs and generates model predictions.
- **Deployed on Google Cloud**: The entire system, including the model and web interface, is hosted on Google Cloud to ensure scalability, reliability, and easy access from anywhere.

## Conclusion

The developed forecasting tool provides investors with a robust method to anticipate gold price changes, aiding in portfolio diversification and risk management strategies. The use of deep learning models has proven effective in capturing complex relationships between gold and various financial indicators.

## Contributors

- Emily Cen
- Linh Chu
- **Ethan Liu (Model Buidling and Training, Front-end Application Development)**
- Joy Sun
