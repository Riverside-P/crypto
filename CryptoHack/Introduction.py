#!/usr/bin/env python3

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


#crypto_message = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#print("Here is your flag:")
#print(base64.b64encode(bytes.fromhex(crypto_message)).decode('utf-8'))

# encrypted_message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print("Here is your flag:")
# print(long_to_bytes(encrypted_message).decode('utf-8'))

# string = "label"
# each = [(ord(c)) for c in string]
# binary_each = [bin(ord(c))[2:] for c in string]
# print("each:", each)
# print("binary_each:", binary_each)
# key = bin(13)[2:]
# print("key:", key)
# new_binary_each = []
# for i in range(len(binary_each)):
#     print(bin(int(binary_each[i], 2)), bin(int(key, 2)))
#     new_binary_each.append(bin(int(binary_each[i], 2) ^ int(key, 2))[2:])
# print("new_binary_each:", new_binary_each)
# new_string = "".join([chr(int(b, 2)) for b in new_binary_each])
# print("new_string:", new_string)
