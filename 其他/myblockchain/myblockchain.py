# author: E41714059 - LiYifei

import hashlib
import json
from argparse import ArgumentParser
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import flask
import requests


class Blockchain:
    def __init__(self):
        self.block_transaction = []
        self.chain = []
        self.neighbor = set()

        # The genesis block
        self.create_block(100, '1')
    
    def create_block(self, nonce, pre_hash):
        """
        Create a new block in the blockchain
        -nonce is a number to solve the POW problem
        return the new block
        """
        
        tranbin = json.dumps(self.block_transaction).encode()
        block = {
            "index": len(self.chain)+1,
            "pre_hash": pre_hash,
            "current_tran_hash": hashlib.sha256(tranbin).hexdigest(),
            "timestamp": time(),
            "nonce": nonce,
            "transactions": self.block_transaction,
        }

        self.block_transaction = []
        self.chain.append(block)

        return block

    def new_transaction(self, start, end, amount):
        """
        Add a trasaction into the next mined block
        
        return the index of block which contains the transaction
        """
        self.block_transaction.append(
            {
                'start': start,
                'end': end,
                'amount': amount,
            }
        )

        return self.chain[-1]['index']+1

    def work_proof(self, last_block):
        """
        Design a simple Proof of Work algorithm
        
        find a number which add to previous nonce, then concatenated hash of previous block
        hash(str(num+nonce)+pre_hash) contains 4 leading zeros.

        return the nonce.
        """
        nonce = 0
        while self.check_proof(last_block["nonce"], nonce, self.Hash(last_block)) == False:
            nonce = nonce+1
        return nonce
    
    def register_neighbor(self, url):
        """
        Add a neighbor. The blockchain program can do conflict check with its neighbors.
        Format: 127.0.0.1(:5000)
        """
        purl = urlparse(url)
        if purl.netloc:
            # input: http://127.0.0.1:5000
            # netloc: 127.0.0.1:5000
            self.neighbor.add(purl.netloc)
        elif purl.path:
            # input: 127.0.0.1:5000 (without scheme)
            # output: 127.0.0.1:5000
            self.neighbor.add(purl.path)

    def resolve_conflict(self):
        """
        Keep all blockchain consistent
        """

        maxlen = len(self.chain)
        repchain = None
        for bk in self.neighbor:
            res = requests.get(f"http://{bk}/showchain")
            if res.status_code==200:
                chainlen = res.json()['length']
                chain = res.json()["blockchain"]

                if chainlen>maxlen:
                    maxlen = chainlen
                    repchain = chain
            
        if repchain:
            self.chain = repchain
            return True

        return False

    
    @staticmethod
    def Hash(block):
        """
        ! only for a block
        """
        blockbin = json.dumps(block, sort_keys=True).encode()
        blockhash = hashlib.sha256(blockbin).hexdigest()
        return blockhash

    @staticmethod
    def check_proof(pre_nonce, nonce, pre_hash):
        """
        return True or False
        """
        concatbin = f'{pre_nonce+nonce}{pre_hash}'.encode()
        concathash = hashlib.sha256(concatbin).hexdigest()

        return concathash[:4] == '0000'

app = flask.Flask(__name__)
node_id = str(uuid4())

blockchain = Blockchain()

@app.route('/showchain', methods=['GET'])
def show_chain():
    res = {
        'blockchain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return flask.jsonify(res), 200

@app.route('/transactions/new', methods=['POST'])
def add_transaction():
    jsondata = flask.request.get_json(force=True)
    value = ['start', 'end', 'amount']
    for k in value:
        if k not in jsondata:
            return "Wrong format", 400
    
    index = blockchain.new_transaction(jsondata['start'], jsondata['end'], jsondata['amount'])
    res = {
        'message': 'Transaction will be added to block '+str(index)
    }
    return flask.jsonify(res), 201

@app.route('/mine', methods=['GET'])
def mine():
    # find nonce
    last_block = blockchain.chain[-1]
    nonce = blockchain.work_proof(last_block)

    # Get a reward
    # Reward transaction will be added to the next block
    # Sender is "0", and amount is set to 1
    blockchain.new_transaction("0", node_id, 1)

    pre_hash = blockchain.Hash(last_block)
    block = blockchain.create_block(nonce, pre_hash)

    res = {
        'message': 'Successful',
        'pre_hash': block['pre_hash'],
        'index': block['index'],
        'timestamp': block['timestamp'],
        'nonce': block['nonce'],
        'transactions': block['transactions'],
    }

    return flask.jsonify(res), 200

@app.route('/neighbor/register', methods=['POST'])
def reg_neighbor():
    values = flask.request.get_json(force=True)
    neighbors = values['neighbor']
    if neighbors is None:
        return "Invalid input", 400
    
    for neighbor in neighbors:
        blockchain.register_neighbor(neighbor)
    
    res = {
        'message': 'new neighbors have been added',
        'total_neighbor': list(blockchain.neighbor),
    }

    return flask.jsonify(res), 200

@app.route('/neighbor/solve', methods=['GET'])
def solve():
    status = blockchain.resolve_conflict()
    if status:
        res = {
            'message': 'Blockchain is replaced',
            'new_chain': blockchain.chain,
        }
    else:
        res = {
            'message': 'do not have to change',
            'chain': blockchain.chain,
        }
    
    return flask.jsonify(res), 200


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help="port to listen on")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)
