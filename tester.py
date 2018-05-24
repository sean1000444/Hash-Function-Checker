import hashlib
import binascii
import x13_hash

from binascii import unhexlify, hexlify

string_hex_version = "06000000"
prev_joined = "0b0f7c52d91e3df5b7365e2a5ca51efb785d18147238d1057586d3d53d44d2eb"
merkle_joined = "16ea42abaf95b69aa91382ce45990b3123729ff09e330c2e994713372eb2cf22"
time_hex = "6f13e05a"
bits_joined = "22fe001d"
nonce_hex = "00000000"

header_hex = (string_hex_version + prev_joined + merkle_joined + time_hex + bits_joined + nonce_hex)
best_hash = '3e331f6e85437e119f7339857f50cd919c5e97100f434f2cd35966f03655f46a'
best_hash_reverse = "".join(reversed([best_hash[i:i+2] for i in range(0, len(best_hash), 2)]))


def tester():
    block_header = unhexlify(header_hex)
    pow_hash = str(hexlify(x13_hash.getPoWHash(block_header)))
    print(pow_hash[2:-1] == best_hash_reverse)
    print(pow_hash[2:-1])
    print(best_hash_reverse)

tester()