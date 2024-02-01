big_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
transformed = ""
for char in big_str:
    if char.isalpha():
        pos = (ord(char.lower()) + 2) % (ord('z') + 1)
        if pos < ord('a'):
            pos += ord('a')
        transformed += chr(pos)
    else:
        transformed += char

url = "map"
table = url.maketrans(big_str, transformed)
print(url.translate(table))

