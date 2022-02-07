import json
from cryptocurrency.blockchain import Blockchain
from cryptocurrency.transaction import Transaction


def main():
	print("Initializing blockchain...")
	blockchain = Blockchain()
	print(json.dumps(blockchain.get_blockchain_content(), indent=4))
	transaction1 = Transaction("A", "B", 10000)
	transaction2 = Transaction("C", "D", 150)
	transaction3 = Transaction("A", "B", 10000)
	transaction4 = Transaction("C", "D", 150)
	blockchain.add_new_transaction(transaction1)
	blockchain.add_new_transaction(transaction2)
	blockchain.add_new_transaction(transaction3)
	blockchain.add_new_transaction(transaction4)
	print("Unverified transactions:")
	print(json.dumps(blockchain.get_unverified_transactions_content(), indent=4))
	blockchain.mine_block()
	print("Blockchain: ")
	print(json.dumps(blockchain.get_blockchain_content(), indent=4))


if __name__ == '__main__':
	main()
