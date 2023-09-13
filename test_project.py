from project import get_key_indicators
from project import get_top

ind_list = [{'Name':'INFY.NS','Market Capitalization':'1000 mn','PE Ratio':'20.14','Dividend Yield':'0.36','Gross Margin':'0.25','PB Ratio':'0.79'},{'Name':'RELIANCE.NS','Market Capitalization':'1100 mn','PE Ratio':'20.01','Dividend Yield':'0.03','Gross Margin':'0.35','PB Ratio':'0.85'},{'Name':'SBIN.NS','Market Capitalization':'998 mn','PE Ratio':'20.65','Dividend Yield':'0.39','Gross Margin':'0.05','PB Ratio':'0.49'}]

def main():
    test_key_ind_count()
    test_get_top()

def test_key_ind_count():
    assert len(get_key_indicators('INFY.NS')) == 6

def test_get_top():
    print(get_top(ind_list,'1'))
    assert get_top(ind_list,'1') == ([{'Name':'RELIANCE.NS','Market Capitalization':'1100 mn','PE Ratio':'20.01','Dividend Yield':'0.03','Gross Margin':'0.35','PB Ratio':'0.85'},{'Name':'INFY.NS','Market Capitalization':'1000 mn','PE Ratio':'20.14','Dividend Yield':'0.36','Gross Margin':'0.25','PB Ratio':'0.79'},{'Name':'SBIN.NS','Market Capitalization':'998 mn','PE Ratio':'20.65','Dividend Yield':'0.39','Gross Margin':'0.05','PB Ratio':'0.49'}], 'Market Capitalization')
    #[('RELIANCE.NS','1100 mn'),('INFY.NS','1000 mn'),('SBIN.NS','998 mn')]
    print(get_top(ind_list,'2'))
    assert get_top(ind_list,'2') == ([{'Name':'RELIANCE.NS','Market Capitalization':'1100 mn','PE Ratio':'20.01','Dividend Yield':'0.03','Gross Margin':'0.35','PB Ratio':'0.85'},{'Name':'INFY.NS','Market Capitalization':'1000 mn','PE Ratio':'20.14','Dividend Yield':'0.36','Gross Margin':'0.25','PB Ratio':'0.79'},{'Name':'SBIN.NS','Market Capitalization':'998 mn','PE Ratio':'20.65','Dividend Yield':'0.39','Gross Margin':'0.05','PB Ratio':'0.49'}], 'PE Ratio')
    #[('RELIANCE.NS','20.01'),('INFY.NS','20.14'),('SBIN.NS','20.65')]

if __name__ == "__main__":
    main()