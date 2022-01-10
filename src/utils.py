from hashlib import sha256


def compute_hash(data):
    sha256(data.encode()).hexdigest()
