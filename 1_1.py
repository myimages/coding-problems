import base64
import binascii

def hex_to_bin(HexStr):
    """
    # Converts hex string to binary literal using python built-in functions
    # TODO convert hex to binary using my own written functions
    PARAMETERS
    HexStr: STRING, a string which represents a number in base 16
    RETURNS
    STRING, it begins with "0b" and then is followed by 0 and 1 digits. This is how Python implements Binary Literals
    """

    return binascii.unhexlify(HexStr)

def bin_to_64(BinaryLit):

    return base64.b64encode(BinaryLit).decode('ascii')


def hex_to_64 (HexStr):
    """
    Convert a hex string to a base64 string.
    """
    BinaryLit  = hex_to_bin(HexStr)
    print(BinaryLit)
    Base64Str = bin_to_64(BinaryLit)
    return Base64Str

# Test
print(hex_to_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
