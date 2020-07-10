import requests

url = 'http://localhost:5000'
url2 = 'http://localhost:5001'

def changeAESkey(newKey:str):
    """
    修改要分发的AES密钥
    """

    with open('./aesKey.key', 'w') as fileObj:
        fileObj.write(newKey)

def setURL(newURL:str):
    """
    设置通信方的URL
    """

    requests.post(url+'/setURL', data=newURL)

def changePlainText(plainText:str):
    """
    修改要用AES加密的明文
    """

    with open('./plaintext.txt', 'w') as fileObj:
        fileObj.write(plainText)

def shareKey():
    """
    密钥分发
    """

    return requests.get(url+'/sendAESkey')

def sndMsg():
    """
    发送消息
    """

    return requests.get(url+'/sendAESmsg')

def getPubKey():
    """
    获取通信方的公钥
    """

    return requests.get(url+'/getPubKey')


if __name__ == "__main__":
    setURL(url2)
    getPubKey()
    changeAESkey('12345678')
    changePlainText('NPU')

    shareKey()
    sndMsg()