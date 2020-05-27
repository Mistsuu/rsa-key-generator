import argparse
from keyparser import importKeyFromFile
from binarystuff import PutDataIntoOneVariable, PutDataIntoString

def encryptFile(filename, public_key):
    print "{*} Encrypting file..."

    # Index of where to find data
    PUBLIC_HALF = 0
    COMMON_HALF = 1
    KEY_LENGTH  = 2

    # Size of buffer to read
    read_size = (public_key[KEY_LENGTH]) / 8 - 2

    try:
        with open(filename, 'rb') as raw_file:
            try:
                with open(filename + ".crypt", 'wb') as encrypted_file:
                    while True:
                        # Read binary buffer from file
                        bufStr = raw_file.read(read_size)
                        if bufStr == b'':
                            break

                        # Convert to a some integer buffer and do the encryption
                        bufVar          = PutDataIntoOneVariable(bufStr, preserveZero=True)
                        encryptedBufVar = pow(bufVar, public_key[PUBLIC_HALF], public_key[COMMON_HALF])
                        encryptedBufStr = PutDataIntoString(encryptedBufVar, public_key[KEY_LENGTH], variableSize=False)
                        # Write to file
                        encrypted_file.write(encryptedBufStr)
                    encrypted_file.close()
            except Exception as err_message:
                print "[Error!] Cannot write to encrypted file!"
                print "* Error message: ", err_message
            raw_file.close()
    except Exception as err_message:
        print "[Error!] Aw man :'( No such file is found..."
        print "* Error message: ", err_message


# Parse user input
# Too lazy to write my own way to parse, sooooo I use a library instead... ~~
parser = argparse.ArgumentParser()
parser.add_argument('-e', '--encrypt', required=True, help="file name of encryption key")
parser.add_argument('-f', '--file',    required=True, help="name of file to encrypt data")
args = parser.parse_args() # If user failed to provide necessary arguments,
                           # this function will end the script

public_key = importKeyFromFile(args.encrypt)
if public_key[2] == -1:
    print "[Error]: Cannot encrypt file!"
else:
    encryptFile(args.file, public_key)
