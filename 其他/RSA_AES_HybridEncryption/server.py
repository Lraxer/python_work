import json
from argparse import ArgumentParser
from urllib.parse import urlparse

import flask
import requests
from flask import Flask

from aes import AES
from readRSAkey import readKey
from rsa import RSA_Decryption, RSA_Encryption

app = Flask(__name__)
# 保存需要用到的数据
app.config['n'] = (readKey())[0]
app.config['e'] = (readKey())[1]
app.config['d'] = (readKey())[2]
app.config['others_n'] = int()
app.config['others_e'] = int()
app.config['aesKey'] = int()
app.config['comURL'] = str()

@app.route('/showPubKey', methods=['GET'])
def showPubKey():
    """
    返回自己的公钥
    """
    
    res = {
        'n': app.config['n'],
        'e': app.config['e'],
    }
    return flask.jsonify(res), 200

@app.route('/getPubKey', methods=['GET'])
def getPubKey():
    """
    请求通信方的公钥
    """

    key = requests.get(app.config['comURL']+'/showPubKey')
    app.config['others_n'] = json.loads(key.text).get('n')
    app.config['others_e'] = json.loads(key.text).get('e')
    return "Successfully get public key", 200

@app.route('/setURL', methods=['POST'])
def setURL():
    """
    设置通信方的IP地址与端口号
    """

    app.config['comURL'] = flask.request.get_data().decode('utf-8')
    return 'Successfully set URL', 201

@app.route('/RSAmsg',  methods=['POST'])
def rcvRSAmsg():
    """
    接收RSA加密的AES密钥并解密保存在aesKey.key
    """

    jsonmsg = flask.request.get_json(force=True)
    rcvMsg = jsonmsg['RSAcipherInt']
    if rcvMsg==0:
        return 'Wrong', 400

    decrypText = RSA_Decryption(rcvMsg, app.config['d'], app.config['n'])
    app.config['aesKey'] = int(decrypText)
    with open('./aesKey.key', 'w') as fileObj:
        fileObj.write(str(app.config['aesKey']))

    return 'Get AES key', 201

@app.route('/AESmsg', methods=['POST'])
def rcvAESmsg():
    """
    接收AES加密的消息并解密保存在plaintext.txt
    """

    jsonmsg = flask.request.get_json(force=True)
    rcvMsg = jsonmsg['AEScipherInt']

    aesdecryp = AES(app.config['aesKey'])
    plainTextInt = aesdecryp.decrypt(rcvMsg)
    plainText = plainTextInt.to_bytes(128, 'big', signed=False).decode('utf-8')
    plainText = plainText.lstrip(b'\x00'.decode('utf-8'))
    with open('./plaintext.txt', 'w') as fileObj:
        fileObj.write(plainText)
    
    return 'Get message', 201

@app.route('/sendAESkey', methods=['GET'])
def sndRSAmsg():
    """
    对AES密钥进行RSA加密并发送
    """

    with open('./aesKey.key', 'r') as fileObj:
        app.config['aesKey'] = int(fileObj.read())
    if app.config['aesKey']==0:
        raise("Can't find AES key.")

    RSAcipher = RSA_Encryption(str(app.config['aesKey']), app.config['others_n'], app.config['others_e'])

    res = {
        'RSAcipherInt': RSAcipher,
    }
    requests.post(app.config['comURL']+'/RSAmsg', data=json.dumps(res))
    return 'Send AES key', 200

@app.route('/sendAESmsg', methods=['GET'])
def sndAESmsg():
    """
    对要发送的消息进行AES加密并发送
    """

    with open('./plaintext.txt', 'r') as fileObj:
        plainText = fileObj.read()
    plainTextByte = plainText.encode('utf-8')
    plainTextInt = int.from_bytes(plainTextByte, 'big', signed=False)
    aesAlgo = AES(app.config['aesKey'])
    cipherTextInt = aesAlgo.encrypt(plainTextInt)

    res = {
        'AEScipherInt': cipherTextInt,
    }
    requests.post(app.config['comURL']+'/AESmsg', data=json.dumps(res))
    return 'Send AES message', 200


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help="port to listen on")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)