# Indian Stock Investment Suggestor

This Python program is an investment analysis tool that fetches key indicators for a list of stocks and provides investment recommendations based on various metrics.
Metrics used are - Market Capitalization, PE Ratio, Dividend Yield, Gross Margin and PB Ratio.
While most data and analysis is available on yfinance, it is tough for anyone to analyse thousands of stocks.
Our Aim is help investors find the safest and best stocks to invest within minutes.


## Disclaimer

These recommendations are generated using only a few inidicators and therefore we provide no guarantees on Return on Investment. User needs to understand that Market Investments are subject to risk.

#### Useful Quotes
To encourage youngsters to invest, some quotes from very profilic people are displayed in the beginning.

#### Video Demo: https://youtu.be/_-3OK_AZT70

#### Audio Script:
Hi I am jeetraj from mumbai, india. My Project is on finding Investment opportunity in the National Stock Exchange of India.​ My Project title is  "Indian Stocks Investment Suggestor" and I have used my knowledge that I acquired from my Masters in Finance as well as my years of experience as a successful Investor. I am sure you already know Stock Market returns are by far the highest when compared to any other investment modes and these days it has become very simple to invest in them.
So, lets start to see what we have in store.
Here is some very fancy ASCII Art to welcome everyone, followed by a very famous investment quote. These quotes change every time you visit us. As you see on the screen we pick up the stocks data from a csv file and fetch all the data for thousands of stocks. This takes around 3 to 5 minutes but for this video, I will speed it up.
So now, we have all the data downloaded and users can select what Indicator do they want to start with for receiving the investment recommendation.
I will select option 1. For which I will be typing 1 and hitting Enter or Return key.
Wonderful, You will get top 10 companies by Market Capitalization. These look very safe to invest in right away. But lets look for more by saying "y" on screen and there you have 10 more stock recommendations.
Wow, I will now say "n" for more recommendations since I want to see other indicators as well.
We need to say "y" for continuing to do our investment research. At this point we can now go to option 2 which is PE or Price to Earning Ratio.
The recommendations based on PE Ratio looks good as these are some undervalued companies.
So now you have an idea how to go on looking at different indicator based recommendations. I challenge you to find out the best stocks to invest using this program and keep coming back for more recommendations since all data analysis happens on latest results posted by companies.

#### Description

The Fundamental Analysis basics are applied to Stock Data and recommendations are produced.
For more knowledge on understanding the Indicators used please read below:
https://investoracademy.org/top-10-fundamental-analysis-indicators-for-all-investors/

The Stock Data is kept in a csv file in the "\projects" folder and can be downloaded from below url and replaced if required.
http://www.nseindia.com/market-data/securities-available-for-trading

User just needs to keep the same file name and replace the existing file in folder.

The program extracts all stock symbols from file and then uses it to fetch data from yfinance module.

Once data is retrieved, all the indicators are analysed. The data is sorted in preference before giving the stock recommendations.

## Usage

1. Install the required dependencies (see `requirements.txt`).
2. Run the `main.py` script to fetch stock data and analyze it.
3. Once the stock data is fetched from yfinance system will ask for choice of indicator.
4. User can select from 1-5.
5. 1 stands for Market Capitalization, 2 for PE Ratio, 3 for Dividend Yield, 4 for Gross Margin and 5 for PB Ratio.
6. Once an output is displayed to user, user can select to continue by saying "y" or discontinue by saying "n".
7. User can go through the top 3 recommendations any number of times for any indicator.

#### Contact in case of suggestions/queries/feedback/job or project opportunity/establish contact

Linkedin Profile : https://www.linkedin.com/in/shahjeetraj/

## Installation

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt