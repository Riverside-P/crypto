

import sys
# import this
import base64
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

# ASCII flag
ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# chr() is the function that converts an integer to its corresponding ASCII character.
# ord() function is the inverse of chr(), converting a character to its ASCII integer value.
# str.join(iterable) is the method that concatenates the elements of the iterable (like a list) into a single string, with "str" as the separator.
# str can be an empty string "" to concatenate without any separator.
print("Here is your flag:")
print("".join(chr(o) for o in ords))

# Hex flag
hex_message = "63727970746f7b4865785f616e645f726561645f62696e6172795f657865725f696e746f5f666c61677d"

# bytes.fromhex() is the function that converts a hexadecimal string into its corresponding byte representation.
# .hex() method is the inverse of bytes.fromhex(), converting bytes back into a hexadecimal string.
# .decode('utf-8') method decodes bytes into a string using UTF-8 encoding.
print("Here is your flag:")
print(bytes.fromhex(hex_message).decode('utf-8'))

# Base64 flag
base64_message = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# base64.b64encode() provided by the base64 module is the function that encodes bytes into a Base64 encoded bytes representation.
# before using base64.b64encode(), make sure to convert the input to bytes.
print("Here is your flag:")
print(base64.b64encode(bytes.fromhex(base64_message)).decode('utf-8'))

# Bytes and Big integer conversion flag
encrypted_message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# long_to_bytes() function provided by the Crypto.Util.number module is the function that converts a big integer into its corresponding byte representation.
# bytes_to_long() function is the inverse of long_to_bytes(), converting bytes back into a big integer.
# before using Crypto functions, make sure to install the pycryptodome library. (run the following command in terminal: pip install pycryptodome)
print("Here is your flag:")
print(long_to_bytes(encrypted_message).decode('utf-8'))

# XOR Starter
string = "label"
parameter = 13

# bin() is the function that converts an integer into its binary string representation, prefixed with '0b'.
# prefix '0b' can be removed by slicing the string [2:].
separated_string_in_binary = [bin(ord(c))[2:] for c in string]
parameter_in_binary = bin(parameter)[2:]

# XOR each bit of the separated string with the parameter
XORed_string_in_binary = []
for i in range(len(separated_string_in_binary)):
    # XOR the current bit with the parameter
    # make sure to convert binary strings back to integers using int(string, 2) before performing XOR operation
    XORed_bit = int(separated_string_in_binary[i], 2) ^ int(parameter_in_binary, 2)
    XORed_string_in_binary.append(XORed_bit)

# Convert the XORed binary values back to characters using chr()
XORed_string = "".join([chr(b) for b in XORed_string_in_binary])
print("Here is your flag:")
print(XORed_string)

# XOR Properties
# XOR makes an abelian group under the operation of bitwise XOR.
# That is, for any bits a, b, and c:
# 1. a ^ b = b ^ a (Commutativity)
# 2. a ^ (b ^ c) = (a ^ b) ^ c (Associativity)
# 3. a ^ 0 = a (Identity)
# 4. a ^ a = 0 (Self-inverse)
# Using these properties, we can reverse the XOR operation.
KEY1 =  "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
the_result_of_XORing_KEY1_and_KEY2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
the_result_of_XORing_KEY2_and_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
the_result_of_XORing_FLAG_KEY1_KEY2_and_KEY3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
def xor_hex_strings(hex1, hex2):
    # Convert hex strings to integers
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    # Perform XOR operation
    xor_result = int1 ^ int2
    # Convert the result back to hex string and remove the '0x' prefix
    return hex(xor_result)[2:]
KEY2 = xor_hex_strings(KEY1, the_result_of_XORing_KEY1_and_KEY2)
KEY3 = xor_hex_strings(KEY2, the_result_of_XORing_KEY2_and_KEY3)
FLAG_HEX = xor_hex_strings(xor_hex_strings(the_result_of_XORing_FLAG_KEY1_KEY2_and_KEY3, the_result_of_XORing_KEY1_and_KEY2), KEY3)
print("Here is your flag:")
print(bytes.fromhex(FLAG_HEX).decode('utf-8'))

# example solution to the above problem
from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag).decode())  

# Favorite byte
given_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded_hex = bytes.fromhex(given_hex)
print(decoded_hex)
for i in range(256):
    xor_result = bytes([b ^ i for b in decoded_hex])
    try:
        if "crypto" in xor_result.decode('utf-8'):
            print("Here is your flag:")
            print(xor_result.decode('utf-8'))
    except UnicodeDecodeError: 
        continue

# You either know, XOR you don't
import math
from collections import Counter

hex_cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
decoded_hex = bytes.fromhex(hex_cipher)

# Crib dragging
crib = b"crypto{"
