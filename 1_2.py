import base64

def fixed_XOR(Hex1, Hex2):
    Bin1= int(Hex1, 16)
    Bin2 = int(Hex2, 16)

    BinXOR= Bin1^Bin2
    HexXOR = hex(BinXOR)
    print(HexXOR)

Hex1 = "1c0111001f010100061a024b53535009181c"
Hex2 = "686974207468652062756c6c277320657965"

fixed_XOR(Hex1, Hex2)
