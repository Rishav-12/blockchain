import hashlib
import time
import json

class Block():
	def __init__(self, index, prev_hash, transactions):
		self.index = index
		self.timestamp = 'time.time()' # We use a string so that the hash does not change everytime we run the program
		self.prev_hash = prev_hash
		self.transactions = transactions
		self.nonce = 0
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		block_data = f'{self.index}{self.timestamp}{self.prev_hash}{json.dumps(self.transactions)}{self.nonce}'
		return hashlib.sha256(block_data.encode()).hexdigest()

	def mine_block(self, difficulty):
		while not self.hash.startswith("0" * difficulty):
			self.nonce += 1
			self.hash = self.calculate_hash()

		print(f"Block mined successfully: {self.hash}")

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
		self.difficulty = 4

	def create_genesis_block(self):
		genesis_block = Block(0, "0", "Initial block")
		self.chain.append(genesis_block)

	def get_last_block(self):
		return self.chain[-1]

	def create_block(self, transactions):
		new_block = Block(self.get_last_block().index + 1, self.get_last_block().hash, transactions)
		new_block.mine_block(self.difficulty)
		self.chain.append(new_block)

	def is_valid(self):
		for i in range(1, len(self.chain)): # We start with index 1 since index 0 is the genesis block
			current_block = self.chain[i]
			prev_block = self.chain[i - 1]

			if current_block.index <= prev_block.index:
				return False

			elif current_block.hash != current_block.calculate_hash():
				return False

			elif current_block.prev_hash != prev_block.hash:
				return False

		return True

def test():
	blockchain = Blockchain()

	blockchain.create_genesis_block()

	print("Mining block 1...")
	blockchain.create_block({ 'sender' : "1", 'recipient' : "Rishav", 'amount' : 4 })

	print("Mining block 2...")
	blockchain.create_block({ 'sender' : "2", 'recipient' : "Sumedha", 'amount' : 6 })

	print("Mining block 3...")
	blockchain.create_block({ 'sender' : "3", 'recipient' : "Tanya", 'amount' : 3 })

	# print(blockchain.chain) # <- uncomment to see details of the blockchain

if __name__ == '__main__':
	test()
