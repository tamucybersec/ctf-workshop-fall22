from pwn import *

CHAL = "login"

p = remote("ctfworkshop.cybr.club", 3005)

# automate inputs as necessary here

p.interactive()
