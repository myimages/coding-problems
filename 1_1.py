def hex_to_bin(HexStr):
    """
    # Converts hex string to binary literal using python built-in functions
    # TODO convert hex to binary using my own written functions
    PARAMETERS
    HexStr: STRING, a string which represents a number in base 16
    RETURNS
    STRING, it begins with "0b" and then is followed by 0 and 1 digits. This is how Python implements Binary Literals
    """

    return bin(int(HexStr, 16))

def bin_to_64(BinaryLit):
    # I can iterate through BinaryLit
    # BL[0] = 0, BL[1] = b

    # Ensures that BinaryLit is a binary literatal
    assert BinaryLit[0:2] == "0b"

    # The Base64 Index Table
    Base64Index = {
    0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E", 5 : "F", 6 : "G", 7 : "H", 8 : "I", 9 : "J", 10 : "K", 11 : "L", 12 : "M", 13 : "N", 14 : "O", 15 : "P", 16 : "Q", 17 : "R", 18 : "S",
    19 : " T", 20 : "U", 21 : "V", 22 : "W", 23 : "X", 24 : "Y", 25 : "Z", 26 : "a", 27 : "b", 28 : "c",
    29 : "d", 30 : "e", 31 : "f", 32 : "g", 33 : "h", 34 : "i", 35 : "j", 36 : "k", 37 : "l", 38 : "m", 39 : "n",
    40 : "o", 41 : "p", 42: "q", 43 : "r", 44 : "s", 45 : "t", 46 : "u", 47 : "v", 48 : "w", 49 : "x", 50 : "y", 51 : "z",
    52 : "0", 53 : "1", 54 : "2", 55 : "3", 56 : "4", 57 : "5", 58 : "6", 59 : "7", 60 : "8", 61 : "9", 62 : "+", 63 : "/"
    }

    # Base Case - Binary Lit contains only 6 bits
    i = 2
    Base64Str = ""
    while i < len(BinaryLit):
        pattern = BinaryLit[i:i + 6]
        Base64Str += Base64Index[int(pattern, 2)]
        i += 6

    return Base64Str

def hex_to_64 (HexStr):
    """
    Convert a hex string to a base64 string.
    Practice Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
    Practice Output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    """
    BinaryLit  = hex_to_bin(HexStr)
    # For building and testing bin_to_64, erase once built
    # The following number represents the integer 19 and in Base64 is T
    BinaryLit = "0b010011"
    Base64Str = bin_to_64(BinaryLit)
    return Base64Str

print(hex_to_64("0xff"))
