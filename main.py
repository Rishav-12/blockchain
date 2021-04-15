import hashlib

class Block():
	def __init__(self, prev_hash, transactions):
		self.prev_hash = prev_hash
		self.transactions = transactions

		self.block_data = '-'.join(self.transactions) + '-' + self.prev_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

	def get_block_hash(self):
		return self.block_hash

class Blockchain():
	def __init__(self):
		self.block_list = []

	def create_genesis_block(self, transactions):
		genesis_block = Block("Initial block", transactions)
		self.block_list.append(genesis_block)

	def create_block(self, transactions):
		new_block = Block(self.block_list[-1].get_block_hash(), transactions)
		self.block_list.append(new_block)

	def get_blockchain_info(self):
		for idx, block in enumerate(self.block_list):
			print(idx, block.get_block_hash())

# Let's take some sample transactions
t1 = "John sends 3.5 coins to Mark"
t2 = "Michael sends 2.2 coins to Harry"
t3 = "Mark sends 5.5 coins to Theo"
t4 = "Michael sends 2.5 coins to Theo"
t5 = "Harry sends 3.4 coins to Dora"
t6 = "Dora sends 4.2 coins to George"
t7 = "Theo sends 4.8 coins to John"
t8 = "Dora sends 5.2 coins to Harry"

blockchain = Blockchain()

blockchain.create_genesis_block([t1, t2])
blockchain.create_block([t3, t4])
blockchain.create_block([t5, t6])
blockchain.create_block([t7, t8])

blockchain.get_blockchain_info()

'''
It can be clearly observed that changing some data in the transactions changes the
hashes of the blocks (try it!) and thus destroy the integrity of the blockchain
'''
