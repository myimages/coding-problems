def hex_to_64 (HexStr):
    """
    Convert a hex string to a base64 string.
    Practice Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    Practice Output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    """

    # Converts hex string to binary literal
    BinaryLit  = bin(int(HexStr, 16))
    print(hex_to_binary(HexStr))
    #return Base64String

hex_to_64("0xff")
