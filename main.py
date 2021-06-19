import hashlib
import time
import json

class Block():
	def __init__(self, index, prev_hash, transactions):
		self.index = index
		self.timestamp = 'time.time()' # We use a string so that the hash does not change everytime we run the program
		self.prev_hash = prev_hash
		self.transactions = transactions
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		block_data = f'{self.index}{self.timestamp}{self.prev_hash}{json.dumps(self.transactions)}'
		return hashlib.sha256(block_data.encode()).hexdigest()

	def __repr__(self):
		return json.dumps({
			'index' : self.index,
			'timestamp' : self.timestamp,
			'previous hash' : self.prev_hash,
			'transactions' : self.transactions,
			'hash' : self.hash
		}, indent = 4)

class Blockchain():
	def __init__(self):
		self.chain = []

	def create_genesis_block(self):
		genesis_block = Block(0, "0", "Initial block")
		self.chain.append(genesis_block)

	def get_last_block(self):
		return self.chain[-1]

	def create_block(self, transactions):
		new_block = Block(self.get_last_block().index + 1, self.get_last_block().hash, transactions)
		self.chain.append(new_block)

blockchain = Blockchain()

blockchain.create_genesis_block()
blockchain.create_block({ 'sender' : "1", 'recipient' : "Rishav", 'amount' : 4 })
blockchain.create_block({ 'sender' : "2", 'recipient' : "Sumedha", 'amount' : 6 })
blockchain.create_block({ 'sender' : "3", 'recipient' : "Tanya", 'amount' : 3 })

print(blockchain.chain)
