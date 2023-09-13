import random
import os
import flag
import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from tabulate import tabulate
from colorama import Fore, Back, Style
from pyfiglet import Figlet
figlet = Figlet(font='ogre')

bold_start = '\033[1m'
bold_end   = '\033[0m'
investing_quotes = ["Invest for the long haul. Don’t get too greedy and don’t get too scared. Shelby M.C. Davis",
                    "The best way to measure your investing success is not by whether you’re beating the market but by whether you’ve put in place a financial plan and a behavioral discipline that are likely to get you where you want to go. Benjamin Graham",
                    "Waiting helps you as an investor and a lot of people just can’t stand to wait. If you didn’t get the deferred-gratification gene, you’ve got to work very hard to overcome that. Charlie Munger",
                    "The stock market is a device to transfer money from the impatient to the patient. Warren Buffett",
                    "Thousands of experts study overbought indicators, head-and-shoulder patterns, put-call ratios, the Fed’s policy on money supply…and they can’t predict markets with any useful consistency, any more than the gizzard squeezers could tell the Roman emperors when the Huns would attack. Peter Lynch",
                    "The function of economic forecasting is to make astrology look respectable. John Kenneth Galbraith",
                    "I make no attempt to forecast the market—my efforts are devoted to finding undervalued securities. Warren Buffett",
                    "Far more money has been lost by investors trying to anticipate corrections, than lost in the corrections themselves. Peter Lynch",
                    "The idea that a bell rings to signal when to get into or out of the stock market is simply not credible. After nearly fifty years in this business, I don’t know anybody who has done it successfully and consistently. I don’t even know anybody who knows anybody who has. Jack Bogle",
                    "Though tempting, trying to time the market is a loser’s game. $10,000 continuously invested in the market over the past 20 years grew to more than $48,000. If you missed just the best 30 days, your investment was reduced to $9,900. Christopher Davis",
                    "History provides a crucial insight regarding market crises: they are inevitable, painful and ultimately surmountable. Shelby M.C. Davis",
                    "A 10% decline in the market is fairly common—it happens about once a year. Investors who realize this are less likely to sell in a panic, and more likely to remain invested, benefitting from the wealthbuilding power of stocks. Christopher Davis",
                    "In the short run, the market is a voting machine. In the long run, it is a weighing machine. Benjamin Graham",
                    "A market downturn doesn’t bother us. It is an opportunity to increase our ownership of great companies with great management at good prices. Warren Buffett",
                    "The intelligent investor is a realist who sells to optimists and buys from pessimists. Benjamin Graham",
                    "You make most of your money in a bear market, you just don’t realize it at the time. Shelby Cullom Davis"]


def main():
    ...
    # GREET AND ADVISE USER
    os.system('clear')
    print(Back.RESET+Fore.GREEN+figlet.renderText("Indian Stocks Investment Suggestor"),(Style.RESET_ALL),end="")
    print("\nHey! Hope your are doing well today.\nHere is a investing quote for you today!")
    print(Fore.BLUE+bold_start+f"{random.choice(investing_quotes)}\n\n",(Style.RESET_ALL)+bold_end)
    # ASK FOR COUNTRY FROM GIVEN CHOICES ONLY
    #user_country = get_user_country()
    print(Fore.MAGENTA+bold_start+f"{flag.flag(':IN:')} India is poised for multipronged growth in the coming times. So start investing in"+Fore.BLUE+" INDIA "+Fore.MAGENTA+"TODAY!!",(Style.RESET_ALL)+bold_end)

    # IMPORT SYMBOLS FROM CSV FILE IN ROOT DIRECTORY
    working_stock_list = get_symbols_from_csv()

    print(bold_start+Fore.MAGENTA+bold_start+f"✋🏽Please wait.. while we are fetching the Data from {len(working_stock_list)} stocks..\nIt sometimes takes around 3-5 minutes.. Be Patient 🤒",(Style.RESET_ALL)+bold_end)

    # GET KEY INDICATORS

    key_indicators = fetch_key_indicators(working_stock_list)
    print(len(key_indicators))
    print(bold_start+Fore.BLUE+"There are many indicators used in Fundamental Analysis. However below 5 are by far the most popular and successful metrics of determining Excellent Investments!!\nConfirm your 1st choice of Indicator: \n You can continue to see Indicators one by one..",(Style.RESET_ALL)+bold_end)
    print(bold_start+Fore.GREEN+"Type 1 for Market Capitalization",(Style.RESET_ALL)+bold_end+"\n Market Capitialization is the total traded value for a given Stock. It determines safety, liquidity and popularity of a stock.")
    print(bold_start+Fore.GREEN+"Type 2 for PE Ratio",(Style.RESET_ALL)+bold_end+"\n PE Ratio is the Price to Earnings multiple whereby a low PE ratio suggests a good potential in Investment. A PE in between 20 to 30 is considered a good measure.")
    print(bold_start+Fore.GREEN+"Type 3 for Dividend Yield",(Style.RESET_ALL)+bold_end+"\n Dividend Yield as an indicator does not work always since many companies reinvest earnings in growth. However many Investors look at high dividend Yields as a sign of strong Financials")
    print(bold_start+Fore.GREEN+"Type 4 for Gross Margin",(Style.RESET_ALL)+bold_end+"\n Gross Margin is an indicator that suggests high margin businesses and thus high returns for investors.")
    print(bold_start+Fore.GREEN+"Type 5 for PB Ratio",(Style.RESET_ALL)+bold_end+"\n PB or price-to-book value is used by investors to gauge whether a company's stock price is valued properly. A P/B ratio of one means that the stock price is trading in line with the book value of the company. A P/B ratio with lower values, particularly those below one, signals to investors that a stock may be undervalued.")
    # ASK TO SELECT INDICATOR TO PROVIDE OUTPUT
    try:
        cont = 'y'
        while cont != 'n':
            more = 'y'
            i=0
            ind_list, ch = get_top(key_indicators,select_indicator())
            print(Fore.CYAN+f"Recommendations as per {ch} leaders:",(Style.RESET_ALL))
            ind_list_new = []
            for j in range(len(ind_list)):
                ind_list_new.append((ind_list[j]['Name'],ind_list[j][ch]))
            while more == 'y' and i < len(ind_list_new):
                print(Fore.CYAN+tabulate(ind_list_new[i:i+11],['Name',ch],tablefmt="fancy_outline"),(Style.RESET_ALL))
                i+=11
                if i < len(ind_list_new):
                    more=get_more()
                else:
                    break
            cont=get_cont()
        else:
            print(Back.RESET+Fore.GREEN+figlet.renderText("Thank you !!"),(Style.RESET_ALL))
            exit()
    except EOFError:
        print(Back.RESET+Fore.GREEN+figlet.renderText("Thank you !!"),(Style.RESET_ALL))
        exit()

def get_symbols_from_csv():
    # Define the path to your CSV file
    csv_file_path = '/workspaces/142012983/project/EQUITY_L .csv'

    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path, usecols=['SYMBOL'])

    # Initialize a list to store the extracted data
    symbols = []

    # Create a progress bar using tqdm
    with tqdm(total=len(df), desc="Extracting Data from csv file") as pbar:
        for symbol in df['SYMBOL']:
            symbols.append(symbol+'.NS')
            pbar.update(1)  # Update the progress bar

    # Now, the 'symbols' list contains the data from the 'SYMBOL' column
    return symbols

def get_key_indicators(stock):

    try:
        ticker = yf.Ticker(stock)
        marketCap = ticker.info.get('marketCap', None)
        peRatio = ticker.info.get('trailingPE', None)
        dividendYield = ticker.info.get('trailingAnnualDividendYield', None)
        grossMargin = ticker.info.get('grossMargins', None)
        bookValue = ticker.info.get('bookValue', None)
        pbRatio = ticker.info['currentPrice'] / bookValue
        return {
                "Name": stock,
                "Market Capitalization": f"{marketCap/1000000:.2f} mn",
                "PE Ratio": f"{peRatio:.2f}",
                "Dividend Yield": f"{dividendYield:.2f}",
                "Gross Margin": f"{grossMargin:.2f}",
                "PB Ratio": f"{pbRatio:.2f}"
            }
    except Exception as e:

        pass

    return None

def fetch_key_indicators(stock_list):
    key_ind_list = []
    # Create a progress bar using tqdm
    with tqdm(total=len(stock_list), desc="Fetching Stock Data") as pbar:
        with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
            futures = [executor.submit(get_key_indicators, stock) for stock in stock_list]

            for future in futures:
                result = future.result()
                if result:
                    key_ind_list.append(result)
                pbar.update(1)  # Update the progress bar

    return key_ind_list

def select_indicator():
    choice = ''
    while choice not in ["1","2","3","4","5"]:
        choice = input("Input Values between 1 and 5: ").strip()
    return choice

def get_top(sil,choice):
    match choice:
        case "1":
            choice = 'Market Capitalization'
            rValue = True
        case "2":
            choice = 'PE Ratio'
            rValue = False
        case "3":
            choice = 'Dividend Yield'
            rValue = True
        case "4":
            choice = 'Gross Margin'
            rValue = True
        case "5":
            choice = 'PB Ratio'
            rValue = False
    # Filter out dictionaries with indicator values greater than 0 & if PE ratio is below 20
    if choice == 'PE Ratio':
        filtered_data = [item for item in sil if float(item[choice]) > 20 and float(item[choice]) < 35]
    elif choice == 'PB Ratio':
        filtered_data = [item for item in sil if float(item[choice]) > 0.00 and float(item[choice]) < 1]
    else:
        filtered_data = [item for item in sil if float(item[choice].replace(' mn', '').replace(',', '')) > 0.00]

    # Sort the list of dictionaries as per above
    sorted_data = sorted(filtered_data, key=lambda x: float(x[choice].replace(' mn', '').replace(',', '')), reverse=rValue)
    #print(sorted_data)
    # Return a list for sorted list
    return sorted_data, choice

def get_cont():
    c=''
    while c.lower().strip() not in ['y','n']:
        c = input("Do you want to continue? type y or n: ")
    return c

def get_more():
    m=''
    while m.lower().strip() not in ['y','n']:
        m = input("Do you want to view more recommendations? type y or n: ")
    return m

if __name__ == "__main__":
    main()