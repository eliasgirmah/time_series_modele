import pandas as pd
import yfinance as yf

def load_stock_data(ticker, start_date, end_date):
    """
    Loads stock data from Yahoo Finance.

    Args:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date in YYYY-MM-DD format.
        end_date (str): The end date in YYYY-MM-DD format.

    Returns:
        pandas.DataFrame: The loaded stock data.
    """

    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def preprocess_data(data):
    """
    Preprocesses the stock data.

    Args:
        data (pandas.DataFrame): The loaded stock data.

    Returns:
        pandas.DataFrame: The preprocessed data.
    """

    # Handle missing values (e.g., fill with interpolation or drop)
    data = data.fillna(method='ffill')

    # Convert the index to a datetime index
    data.index = pd.to_datetime(data.index)

    return data

# Example usage:
ticker = "TSLA"
start_date = "2015-01-01"
end_date = "2024-10-31"

data = load_stock_data(ticker, start_date, end_date)
preprocessed_data = preprocess_data(data)

print(preprocessed_data.head())