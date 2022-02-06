import json
from hashlib import sha256
from typing import List, Dict, Type


def compute_hash(data: str) -> str:
	return sha256(data.encode()).hexdigest()


def dicts_to_strings(list_of_dicts: List[Dict]) -> List[str]:
	list_of_strings = []
	for i in list_of_dicts:
		list_of_strings.append(json.dumps(i))
	return list_of_strings
