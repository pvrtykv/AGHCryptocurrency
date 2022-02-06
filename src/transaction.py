import json
from typing import Dict


class Transaction:
	def __init__(self, sender: str, recipient: str, amount: float):
		self.sender = sender,
		self.recipient = recipient,
		self.amount = amount

	def get_transaction_data(self) -> Dict:
		return {
			"sender": self.sender,
			"recipient": self.recipient,
			"amount": self.amount
		}
