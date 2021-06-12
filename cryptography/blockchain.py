from cryptography.hazmat.primitives import hashes
import hashlib

digest=hashes.Hash(hashes.SHA256(),)
digest.update(b'2dfhas')
hash=digest.finalize()
print(hash)


hash=hashlib.sha256(str('2dfhas').encode()).hexdigest()
print(hash)