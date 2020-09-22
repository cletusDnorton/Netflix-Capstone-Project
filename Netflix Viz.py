#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
netflix_stocks = pd.read_csv('NFLX.csv')
netflix_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)
print(netflix_stocks.head())


# In[2]:


dowjones_stocks = pd.read_csv('DJI.csv')
dowjones_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)
print(dowjones_stocks.head())


# In[3]:


netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'}, inplace=True)
print(netflix_stocks_quarterly.head())


# In[4]:


ax = sns.violinplot(data = netflix_stocks_quarterly, x= 'Quarter', y= 'Price')
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
ax.set_ylabel('Closing Stock Price')
ax.set_xlabel('Business Quarters in 2017')
plt.show()
plt.savefig('Netflix stock by Qtr.png')


# In[5]:


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]
plt.scatter(x_positions, earnings_actual, c= 'red', alpha = 0.5)
plt.scatter(x_positions, earnings_estimate, c= 'blue', alpha = 0.5)
plt.legend(['Actual', 'Estimate'], loc=4)
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')
plt.show()
plt.savefig('Earnings per Share.png')


# In[6]:


revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]
n = 1
t = 2
d = 4
w = 0.8
bars1_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars1_x, revenue_by_quarter)

n = 2
t = 2 
d = 4 
w = 0.8
bars2_x = [t*element + w*n for element
             in range(d)]
middle_x = [(x1 + x2)/2.0 for (x1, x2) in zip(bars1_x, bars2_x)]
plt.bar(bars2_x, earnings_by_quarter)
plt.legend(['Revenue', 'Earnings'])
plt.title('Revenue Vs Earning by Qtr in Billions of Dollars')
plt.xticks(middle_x, quarter_labels)
plt.show()
plt.savefig('Revenue Vs Earnings.png')


# In[7]:


plt.subplot(1,2,1)
ax1= plt.subplot(1,2,1)
plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xlabel('Date Netflix')
ax1.set_ylabel('Netflix Stock Price')
ax1.set_xticks(netflix_stocks['Date'])
ax1.set_xticklabels(netflix_stocks['Date'], rotation = 75)

plt.subplot(1,2,2)
ax2= plt.subplot(1,2,2)
plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xlabel('Date Dow')
ax2.set_ylabel('Dow Stock Price')
ax2.set_xticks(dowjones_stocks['Date'])
ax2.set_xticklabels(dowjones_stocks['Date'], rotation = 75)
plt.subplots_adjust(wspace=.5)
plt.show()
plt.savefig('Netflix vs Dow.png')


# In[ ]:




