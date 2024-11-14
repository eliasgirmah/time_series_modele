import unittest
import pandas as pd
from unittest.mock import patch
from data_loading import load_stock_data, preprocess_data
set PYTHONPATH=%cd%

class TestDataLoad(unittest.TestCase):

    @patch('dataload.yf.download')
    def test_load_stock_data(self, mock_yf_download):
        # Mock data to simulate Yahoo Finance data
        mock_data = pd.DataFrame({
            'Open': [100, 101, 102],
            'High': [110, 111, 112],
            'Low': [99, 100, 101],
            'Close': [109, 110, 111],
            'Volume': [1000, 1500, 1200]
        }, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))
        
        mock_yf_download.return_value = mock_data

        # Call the function
        ticker = "TSLA"
        start_date = "2023-01-01"
        end_date = "2023-01-03"
        data = load_stock_data(ticker, start_date, end_date)

        # Assertions
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)
        self.assertListEqual(list(data.columns), ['Open', 'High', 'Low', 'Close', 'Volume'])

    def test_preprocess_data(self):
        # Sample data with NaN values
        data = pd.DataFrame({
            'Open': [100, None, 102],
            'High': [110, 111, None],
            'Low': [99, None, 101],
            'Close': [109, 110, 111],
            'Volume': [1000, None, 1200]
        }, index=pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']))

        # Preprocess the data
        processed_data = preprocess_data(data)

        # Check if NaN values are forward filled
        self.assertFalse(processed_data.isnull().values.any())

        # Check if the index is a datetime index
        self.assertTrue(isinstance(processed_data.index, pd.DatetimeIndex))

if __name__ == "__main__":
    unittest.main()
