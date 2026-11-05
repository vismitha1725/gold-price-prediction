# Gold ETF Price Prediction

## Project Overview
This project uses Machine Learning techniques to analyse and predict the next observation's Gold ETF (GLD) price based on financial indicators.

The project uses Linear Regression and Random Forest Regression and compares their performance using different train-test splitting methods.

## Dataset
The dataset contains 2,290 observations and the following features:
- SPX – S&P 500 index
- GLD – Gold ETF price
- USO – United States Oil Fund
- SLV – Silver ETF price
- EUR/USD – Euro to US Dollar exchange rate

Source: Kaggle – Gold Price Data

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Machine Learning Models
- Linear Regression
- Random Forest Regressor
- Persistence Baseline for forecasting comparison

## Key Findings
- Random Forest achieved an R² score of approximately 0.99 with a random train-test split.
- Chronological validation showed substantially weaker generalisation.
- For next-observation forecasting, the persistence baseline outperformed Random Forest.
- Additional historical features did not improve Random Forest performance in this experiment.

## Application
A simple Streamlit application allows users to enter financial indicators and obtain a predicted next GLD price.

## How to Run

1. Clone the repository.
2. Install dependencies:

   pip install -r requirements.txt

3. Run the application:

   streamlit run app.py

## Disclaimer
This is an educational machine learning project. Predictions are experimental and should not be used for financial decisions.

The dataset contains GLD ETF prices, not Indian retail gold prices.