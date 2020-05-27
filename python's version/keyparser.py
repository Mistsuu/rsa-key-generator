import base64
from binarystuff import PutDataIntoString, PutDataIntoOneVariable

def writeKeyToFile(filename, key):
    try:
        key_file = open(filename, 'w')
        key_file.write(base64.b64encode(PutDataIntoString(key[0])))
        key_file.write("\n")
        key_file.write(base64.b64encode(PutDataIntoString(key[1])))
        key_file.write("\n")
        key_file.write(base64.b64encode(PutDataIntoString(key[2])))
        key_file.write("\n")
        key_file.close()
        return True
    except Exception as err_message:
        print "[Error!] Cannot open file to write key!"
        print "* Error message: ", err_message
        return False

def importKeyFromFile(filename):
    try:
        key_file = open(filename, 'r')
        uncommon_half = PutDataIntoOneVariable(base64.b64decode(key_file.readline()), preserveZero=False)
        common_half   = PutDataIntoOneVariable(base64.b64decode(key_file.readline()), preserveZero=False)
        key_length    = PutDataIntoOneVariable(base64.b64decode(key_file.readline()), preserveZero=False)
        return uncommon_half, common_half, key_length
    except Exception as err_message:
        print "[Error!] Cannot import key from file!"
        print "* Error message: ", err_message
        return -1, -1, -1
    return 0
