from flask import Flask,jsonify,request
import hashlib
import datetime
import json
from uuid import uuid4
form urllib.parse import urlparse
import requests

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(nonce=1, prev_hash=0)
    
    def create_block(self, nonce, prev_hash):
        block={'index':len(self.chain)+1,
               'timestamp':str(datetime.datetime.now()),
               'nonce':nonce, 
               'prev_hash':prev_hash
              }
        self.chain.append(block)
        return block
    
    def get_prev_block(self):
        return self.chain[-1]


    def proof_of_work(self,prev_nonce):
        new_nonce=1
        while True:
            hash_operation=hashlib.sha256(str(new_nonce**2 - prev_nonce**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                break
            new_nonce+=1
        
        return new_nonce
  
    def hash(self, block):
        encoded_string=json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_string).hexdigest()
    


blockchain=Blockchain()


my_app=Flask(__name__)
@my_app.route('/mine',methods=['GET'])
def mine():
    prev_block=blockchain.get_prev_block()
    nonce=blockchain.proof_of_work(prev_block['nonce'])
    prev_hash=blockchain.hash(prev_block)
    block=blockchain.create_block(nonce,prev_hash)

    response={
              'message':'Congo you just mined a block',
              'index': block['index'],
              'nonce':block['nonce'],
              'timestamp':block['timestamp'],
              'prev_hash':block['prev_hash']
             }
    return jsonify(response),200


@my_app.route('/getchain',methods=['GET'])
def get_chain():
    response= {
                'chain':blockchain.chain,
                'length':len(blockchain.chain)
              }
    return jsonify(response),200

my_app.run(host='0.0.0.0',port=9999)





