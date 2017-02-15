import base64

bin1= int("1c0111001f010100061a024b53535009181c", 16)
bin2 = int("686974207468652062756c6c277320657965", 16)

answer = bin1^bin2

print("%x" % answer)
