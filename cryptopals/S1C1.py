import base64

def hex_to_bin(HexStr):
    """
    Converts a hex string into a binary literal
    """
    return base64.b16decode(HexStr, casefold = True)

def bin_to_64(BinaryLit):
    """
    Converts a binary literal into a base64 string.
    """
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
#print(hex_to_64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")
