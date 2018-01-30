import requests

def search(keyword):
    try:
        kv = {'wd': keyword}
        r = requests.get('http://www.baidu.com/s', params=kv)
        print(r.request.url)
        r.raise_for_status()
    except:
        print('Failed to get information from ' + r.request.url)
    else:
        return r.text[:1000]

if __name__ == '__main__':
    k = input('Input the keyword:\n')
    v = search(k)
    print(v)
