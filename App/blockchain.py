import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
transactionone = blockchain.new_transaction("DOGE", "Ivan", '0.50 BTC')
transactiontwo = blockchain.new_transaction("USDT", "Georgi", '0.05 BTC')
transactionthree = blockchain.new_transaction("BTC", "Petar", '0.10 BTC')
blockchain.new_block(12345)

transactionfour = blockchain.new_transaction("SHIB", "Alisia", '1 BTC')
transactionfive = blockchain.new_transaction("LTC", "Pavlina", '0.892 BTC')
transactionsix = blockchain.new_transaction("BNB", "Maria", '0.5 BTC')
blockchain.new_block(6789)

print("Example block: ", blockchain.chain)
