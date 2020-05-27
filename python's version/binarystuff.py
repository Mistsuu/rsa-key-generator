from random import randrange

def PutDataIntoOneVariable(bufStr, preserveZero=True):
    bufVar = 0                       # Put 0 in front of data if we're not afraid of losing possible leading 0s
    if preserveZero:
        bufVar = randrange(1, 256)   # Put any non-zero number in data in order to prevent the loss of leading 0
                                     # Better encryption, maybe?
    for chr in bufStr:
        bufVar = (bufVar << 8) | ord(chr)
    return bufVar

def PutDataIntoString(bufVar, length=1024, variableSize=True):
    bufStr = b''
    if variableSize:
        while bufVar > 0:
            bufStr = str(chr(bufVar & 0xff)) + bufStr
            bufVar = bufVar >> 8
    else:
        for i in range(0, length / 8):
            bufStr = str(chr(bufVar & 0xff)) + bufStr
            bufVar = bufVar >> 8
    return bufStr
