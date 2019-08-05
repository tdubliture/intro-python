"""
learn about bytes
bytes are similar to str type, but they are a sequence of
bytes instead of unicode code points

use for raw binary data fixed width and single byte encoding : ASCII
use the byte() constructor
"""

d = b'data'
print(d, type(d))

info = b'some bytes here'
#split the bytes using split() built in

print(info.split())

# encoding alt+ 162 ó
message = "vamos al zoológico"
print(message)
data = message.encode("utf-8")
print(data)

#decoding the string
new_message = data.decode("utf-8")
print(new_message)

