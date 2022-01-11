from hashlib import sha256


def compute_hash(data):
    return sha256(data.encode()).hexdigest()


