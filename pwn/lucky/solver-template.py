from pwn import *

CHAL = "lucky"

p = remote("ctfworkshop.cybr.club", 3002)

# automate inputs as necessary here

p.interactive()
