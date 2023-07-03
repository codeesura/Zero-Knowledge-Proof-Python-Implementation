import hashlib
import os
import random

class ZKProof:
    def __init__(self):
        self.N = 20
        self.salt = os.urandom(16)

    def _hash(self, x):
        return hashlib.sha256(x.encode('utf-8') + self.salt).hexdigest()

    def generate_proof(self, secret):
        self.secret = secret
        self.v = self._hash(secret)
        r = str(random.randint(1, self.N))
        self.x = self._hash(r)
        return self.x

    def get_secret(self):
        return self.secret

    def verify(self, response):
        return self.v == self._hash(response)

zkp = ZKProof()

secret_card = 'spade_two' # Here we define the secret card
x = zkp.generate_proof(secret_card)
print('Proof:', x)

response = input('Enter the card to verify: ')
print('Verified:', zkp.verify(response))
