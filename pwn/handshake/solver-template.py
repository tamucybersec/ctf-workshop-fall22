from pwn import *

CHAL = "handshake"

p = remote("ctfworkshop.cybr.club", 3004)

# automate inputs as necessary here

p.interactive()
