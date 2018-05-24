import hashlib
import binascii
import x13_hash

from binascii import unhexlify, hexlify

little_version = (6).to_bytes(4, "little")
string_hex_version = (binascii.hexlify(little_version))

previous_hash = "ebd2443dd5d3867505d1387214185d78fb1ea55c2a5e36b7f53d1ed9527c0f0b"
prev_joined = "".join(reversed([previous_hash[i:i+2] for i in range(0, len(previous_hash), 2)]))

merkle_hash = "22cfb22e371347992e0c339ef09f7223310b9945ce8213a99ab695afab42ea16"
merkle_joined = "".join(reversed([merkle_hash[i:i+2] for i in range(0, len(merkle_hash), 2)]))

time_bytes = (1524634479).to_bytes(4, "little")
time_hex = (binascii.hexlify(time_bytes))

bits_hex = "1d00fe22"
bits_joined = "".join(reversed([bits_hex[i:i+2] for i in range(0, len(bits_hex), 2)]))

nonce_bytes = (2504433986).to_bytes(4, "little")
nonce_hex = (binascii.hexlify(nonce_bytes))

print(string_hex_version)
print(prev_joined)
print(merkle_joined)
print(time_hex)
print(bits_joined)
print(nonce_hex)