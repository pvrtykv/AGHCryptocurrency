from blockchain import Blockchain
from transaction import Transaction

blockchain = Blockchain()

transaction = Transaction("A", "B", 10000)
blockchain.add_new_transaction(transaction)
blockchain.mine_block()
