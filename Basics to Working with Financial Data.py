'''
@author: tdailey

importing needed packeages
'''

#import pandas as pd ;pandas allows for data manipulation (not needed)
#import numpy as np ;numerical python allows for data analysis (not needed)

'''
#need to run 'pip install yfinance' in console
#need to run 'pip install plotly' in console
'''

import yfinance as yf #Yahoo Finance for financial and stock data
import matplotlib.pyplot as plt #graphing tool used for python
import plotly.graph_objects as go
import plotly.io as pio



# =============================================================================
# Downloading Financial Data ; example, Apple Stock
# =============================================================================

ticker= 'AAPL' #slect the company Ticker you want and set it to variable 'ticker'
data= yf.download(ticker,
                  start='2025-10-09',
                  end='2026-10-09',
                  multi_level_index= False) #getting 1-year of data for the ticker
                                #(Apple) and setting it to variable called 'data' 
data.head() #shows the first 5 rows for the data stored in variable 'data'



# =============================================================================
# Basic Price Chart Visualization
# =============================================================================
plt.figure(figsize=(10,6)) #deciding how large the chart will be by setting size
plt.plot(data.index, data['Close'], label = 'Closing Price')
    #plotting the 'data' variable starting with index/position then chosing column 
    #that will be measured and labeling the line.
plt.xlabel('Date') #give X-axis a label
plt.ylabel("Price ($)") #giving Y-axis a label
plt.title(f'{ticker} Closing Price') #setting title for chart
plt.legend() 
plt.grid(True)
plt.show() #Needed for the chart to be shown



# =============================================================================
# Basic Financial Calulations
# =============================================================================

data['Returns'] = data['Close'].pct_change() #adding a column to the 'data' variable
    # called 'Returns' that stores percent chg betweeen closing price ('Close').
data.head() 

data['Cumulative Returns'] = (1+ data['Returns']).cumprod()-1
    #adding another column that calulates the cumulative return
        #which is each return added on top of each other


# =============================================================================
# Some Basic Statistics
# =============================================================================

avg_daily_return= data['Returns'].mean() #Calculates the Average daily asset return
avg_daily_return

daily_vol= data['Returns'].std() #Calculates the Standard Deviaition of return

annualized_return=  (1+avg_daily_return)**252 -1 #Calculates total return
annualized_return



# =============================================================================
# Another Matplotlib Visual for Returns
# =============================================================================
plt.figure(figsize=(10,6))
plt.plot(data.index, data['Returns'], label='Daily Returns', color='blue')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.title(f'{ticker} Daily Returns')
plt.legend()
plt.grid(True)
plt.show()



# =============================================================================
# Plotly ; More Interactive Chart Type
# =============================================================================
pio.renderers.default= 'browser' #Setting it to open in Browser

fig= go.Figure(data= [go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])
    #allows for candlestick graphs which show more information about the asset
    #using the columns from the 'data' variable

fig.update_layout(title=f'{ticker} Candlestick Chart',
                  xaxis_title= 'Date',
                  yaxis_title= 'Price ($)',
                  template= 'plotly_dark',
                  xaxis_rangeslider_visible= False)
    #Setting the graph tiles and axis' along with setting color.

fig.show() #needed for chart to show
    
    
    
