from pwn import *

CHAL = "variable_overwrite"

p = remote("ctfworkshop.cybr.club", 3001)

# automate inputs as necessary here

p.interactive()
