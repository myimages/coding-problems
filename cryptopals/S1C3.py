import S1C1
import S1C2
from string import ascii_lowercase

def single_byte_XOR_cypher(ciphertext):
    """
    Decrypts a hex encoded string that was encrypted by being XORd against a single character.
    """
    for c in ascii_lowercase:
        c_hex = hex(ord(c))
        S1C2.fixed_XOR(ciphertext, c_hex)

single_byte_XOR_cypher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

