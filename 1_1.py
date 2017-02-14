def hex_to_bin(HexStr):
    """
    # Converts hex string to binary literal using python built-in functions
    # TODO convert hex to binary using my own written functions
    PARAMETERS
    HexStr: STRING, a string which represents a number in base 16
    """

    return bin(int(HexStr, 16))

def bin_to_64(BinaryLit):
    # I can iterate through BinaryLit
    # BL[0] = 0, BL[1] = b
    print(BinaryLit[1])
    Base64Str = "placeholder"
    return Base64Str

def hex_to_64 (HexStr):
    """
    Convert a hex string to a base64 string.
    Practice Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    Practice Output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    """
    BinaryLit  = hex_to_bin(HexStr)
    print(str(BinaryLit))
    Base64Str = bin_to_64(BinaryLit)
    return Base64Str

hex_to_64("0xff")
