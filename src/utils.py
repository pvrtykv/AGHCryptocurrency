from hashlib import sha256


def calculate_hash(data):
    sha256(data.encode()).hexdigest()
