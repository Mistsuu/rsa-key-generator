import argparse
from rsa import generate_keys
from keyparser import writeKeyToFile

# Parse user input
# Too lazy to write my own way to parse, sooooo I use a library instead... ~~
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', type=int, default=1024, help="length of the key (default is 1024 bits)")
parser.add_argument('-e', '--encrypt', required=True, help="name of the output file to encrypt")
parser.add_argument('-d', '--decrypt', required=True, help="name of the output file to decrypt")
args = parser.parse_args() # If user failed to provide necessary arguments,
                           # this function will end the script

# Generate the public & private keys
print "{*} Generating keys with length", args.length, "... (This is gonna be tough >:( )"
public_key, private_key = generate_keys(args.length)

# Write them to a file
print "{*} Finish generating... Write them to a file... (Almost done ~~)"
if not writeKeyToFile(args.encrypt, public_key):
    print "[Error!] Cannot write public key to \"", args.encrypt,"\"! (Aw man :'( )"
else:
    print "{*} Public  key written successfully to \"", args.encrypt,"\" !! (Yeyy :D )"
    
if not writeKeyToFile(args.decrypt, private_key):
    print "[Error!] Cannot write private key to \"", args.decrypt,"\"! (Aw man :'( )"
else:
    print "{*} Private key written successfully to \"", args.decrypt,"\" !! (Yeyy :D )"
