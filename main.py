import pandas as pd
import numpy as np
 #import talib as tb
 #import pandas_ta as ta
import ta as ta
from backtester import BackTester


def process_data(data):
    # Compute moving averages using past and current data (no lookahead)
    data['SMA_FAST'] = data['close'].rolling(window=10).mean()
    data['SMA_SLOW'] = data['close'].rolling(window=50).mean()
    return data


def strat(data):
    # Generate signals based on SMA crossover
    data['signals'] = 0
    data['trade_type'] = 'HOLD'
    position = 0

    for i in range(50, len(data)):
        fast_now = data.loc[i, 'SMA_FAST']
        slow_now = data.loc[i, 'SMA_SLOW']
        fast_prev = data.loc[i - 1, 'SMA_FAST']
        slow_prev = data.loc[i - 1, 'SMA_SLOW']

        if position == 0:
            if fast_now > slow_now and fast_prev <= slow_prev:
                data.loc[i, 'signals'] = 1
                data.loc[i, 'trade_type'] = 'LONG'
                position = 1
            elif fast_now < slow_now and fast_prev >= slow_prev:
                data.loc[i, 'signals'] = -1
                data.loc[i, 'trade_type'] = 'SHORT'
                position = -1

        elif position == 1:
            if fast_now < slow_now and fast_prev >= slow_prev:
                data.loc[i, 'signals'] = -1
                data.loc[i, 'trade_type'] = 'CLOSE'
                position = 0

        elif position == -1:
            if fast_now > slow_now and fast_prev <= slow_prev:
                data.loc[i, 'signals'] = 1
                data.loc[i, 'trade_type'] = 'CLOSE'
                position = 0

    return data



def main():
    data = pd.read_csv("BTC_2019_2023_1d.csv")
    processed_data = process_data(data) # process the data
    result_data = strat(processed_data) # Apply the strategy
    csv_file_path = "final_data.csv" 
    result_data.to_csv(csv_file_path, index=False)

    bt = BackTester("BTC", signal_data_path="final_data.csv", master_file_path="final_data.csv", compound_flag=1)
    bt.get_trades(1000)

    # print trades and their PnL
    for trade in bt.trades: 
        print(trade)
        print(trade.pnl())

    # Print results
    stats = bt.get_statistics()
    for key, val in stats.items():
        print(key, ":", val)


    #Check for lookahead bias
    print("Checking for lookahead bias...")
    lookahead_bias = False
    for i in range(len(result_data)):
        if result_data.loc[i, 'signals'] != 0:  # If there's a signal
            temp_data = data.iloc[:i+1].copy()  # Take data only up to that point
            temp_data = process_data(temp_data) # process the data
            temp_data = strat(temp_data) # Re-run strategy
            if temp_data.loc[i, 'signals'] != result_data.loc[i, 'signals']:
                print(f"Lookahead bias detected at index {i}")
                lookahead_bias = True

    if not lookahead_bias:
        print("No lookahead bias detected.")

    # Generate the PnL graph
    bt.make_trade_graph()
    bt.make_pnl_graph()
    
if __name__ == "__main__":
    main()