import argparse
from keyparser import importKeyFromFile
from binarystuff import PutDataIntoOneVariable, PutDataIntoString

def decryptFile(filename, private_key):
    print "{*} Decrypting file..."

    PRIVATE_HALF = 0
    COMMON_HALF  = 1
    KEY_LENGTH   = 2

    read_size = private_key[KEY_LENGTH] / 8
    try:
        with open(filename, 'rb') as raw_file:
            try:
                with open(filename + ".decrypt", 'wb') as decrypted_file:
                    while True:
                        # Read binary buffer from file
                        bufStr = raw_file.read(read_size)
                        if bufStr == b'':
                            break

                        # Convert to a 1024-bit integer buffer and do the encryption
                        bufVar          = PutDataIntoOneVariable(bufStr, preserveZero=False)
                        decryptedBufVar = pow(bufVar, private_key[PRIVATE_HALF], private_key[COMMON_HALF])
                        decryptedBufStr = PutDataIntoString(decryptedBufVar)

                        # Write to file
                        decrypted_file.write(decryptedBufStr[1:])
                    decrypted_file.close()
            except Exception as err_message:
                print "[Error!] Cannot write to decrypted file!"
                print "* Error message: ", err_message
            raw_file.close()
    except Exception as err_message:
        print "[Error!] Aw man :'( No such file is found..."
        print "* Error message: ", err_message


# Parse user input
# Too lazy to write my own way to parse, sooooo I use a library instead... ~~
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--decrypt', required=True, help="file name of decryption key")
parser.add_argument('-f', '--file',    required=True, help="name of file to decrypt data")
args = parser.parse_args() # If user failed to provide necessary arguments,
                           # this function will end the script

private_key = importKeyFromFile(args.decrypt)
if private_key[2] == -1:
    print "[Error]: Cannot decrypt file!"
else:
    decryptFile(args.file, private_key)
