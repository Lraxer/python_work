import requests

def getHTMLText(url):
    # 检验网站的状态码，是200则获取信息
    try:
        r = requests.get(url, timeout=30)   #30s后停止等待响应
        r.raise_for_status()    #状态码不是200则引发HTTPError异常
    except:
        return 'Failed to get information from ' + url + '.'
    else:
        r.encoding = r.apparent_encoding
        return r.text

if __name__ == '__main__':
    url = input("Input the url:\n")
    print(getHTMLText(url))
