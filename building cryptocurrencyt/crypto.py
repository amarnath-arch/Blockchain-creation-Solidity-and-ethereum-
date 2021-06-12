import hashlib
from flask import Flask,jsonify,request
import json
import datetime
import requests
from uuid import uuid4
from urllib.parse import urlparse

class Blockchain:

    def __init__(self):
        self.chain=[]
        self.create_block(nonce=1,prev_hash=0)
    
    def create_block(self,nonce,prev_hash):
        

if __name__=="__main__":
