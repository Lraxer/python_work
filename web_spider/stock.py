import requests
import re
import traceback
from bs4 import BeautifulSoup

def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ''

def getStockName(lst, stock_url):
    text = getHTMLText(stock_url, 'GB2312')
    soup = BeautifulSoup(text, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue

def getStockInfo(lst, info_url, fpath):
    count = 0
    for stock in lst:
        infoUrl = info_url + stock + '.html'
        html = getHTMLText(infoUrl)
        try:
            if html=='':
                continue
            stockDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            name = stockInfo.find_all('a', attrs={'class':'bets-name'})[0]      #这里a可以不加
            stockDict.update({'股票名称':name.text.split()[0]})

            keylist = soup.find_all('dt')
            valuelist = soup.find_all('dd')
            for i in range(len(keylist)):
                key = keylist[i].text
                value = valuelist[i].text
                stockDict[key] = value
            
            with open(fpath, 'a', encoding='utf-8') as file:
                file.write(str(stockDict)+'\n')
                count += 1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)), end="")
        except:
            count += 1
            print('\r当前进度：{:.2f}%'.format(count*100/len(lst)), end="")
            continue

def main():
    stock_name_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    fpath = 'F:/stock.txt'
    lst = []
    getStockName(lst, stock_name_url)
    getStockInfo(lst, stock_info_url, fpath)


main()