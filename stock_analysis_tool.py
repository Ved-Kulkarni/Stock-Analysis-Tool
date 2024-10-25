import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

def stock_price_analysis(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Adj Close'], label='Adjusted Close Price')
    plt.title('Stock Price Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def moving_average_analysis(stock_data):
    stock_data['MA50'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Adj Close'].rolling(window=200).mean()

    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Adj Close'], label='Adjusted Close Price')
    plt.plot(stock_data['MA50'], label='50-Day Moving Average')
    plt.plot(stock_data['MA200'], label='200-Day Moving Average')
    plt.title('Moving Average Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def volume_analysis(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Volume'], label='Volume')
    plt.title('Volume Analysis')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.grid(True)
    plt.show()

def linear_regression_analysis(stock_data):
    adj_close_prices = stock_data['Adj Close'].values
    x = np.arange(len(adj_close_prices)).reshape(-1, 1)
    y = adj_close_prices.reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)
    trend_line = model.predict(x)

    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, adj_close_prices, label='Adjusted Close Price')
    plt.plot(stock_data.index, trend_line, label='Trend Line', linestyle='--')
    plt.title('Linear Regression Analysis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    stock_symbol = ""
    while stock_symbol != "END":
        stock_symbol = input("Enter the stock symbol (e.g., RELIANCE.NS for Reliance Industries, or 'END' to exit): ")
        if stock_symbol == "END":
            break

        start_date_str = input("Enter the start date (DD-MM-YYYY): ")
        start_date = datetime.datetime.strptime(start_date_str, "%d-%m-%Y")
        end_date_str = input("Enter the end date (DD-MM-YYYY): ")
        end_date = datetime.datetime.strptime(end_date_str, "%d-%m-%Y")

        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

        df = pd.DataFrame(stock_data)
        print("First few rows of the DataFrame:")
        print(df.head())
        option = 0
        while option != 5:
            print("Select analysis option:")
            print("1. Stock Price Analysis")
            print("2. Moving Average Analysis")
            print("3. Volume Analysis")
            print("4. Linear Regression Analysis")
            print("5. Exit")

            option = int(input("Enter option number: "))

            switch = {
                1: stock_price_analysis,
                2: moving_average_analysis,
                3: volume_analysis,
                4: linear_regression_analysis,
            }

            analysis_function = switch.get(option, lambda x: None)
            if analysis_function:
                analysis_function(stock_data)

if __name__ == "__main__":
    main()
