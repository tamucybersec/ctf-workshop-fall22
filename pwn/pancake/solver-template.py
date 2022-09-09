from pwn import *

CHAL = "pancake"

p = remote("ctfworkshop.cybr.club", 3000)

# automate inputs as necessary here

p.interactive()
