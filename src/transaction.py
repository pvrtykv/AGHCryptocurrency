import json


class Transaction:
	def __init__(self, sender, recipient, amount):
		self.sender = sender,
		self.recipient = recipient,
		self.amount = amount

	def get_transaction_data(self):
		return json.dumps({
			"sender": self.sender,
			"recipient": self.recipient,
			"amount": self.amount
		})
