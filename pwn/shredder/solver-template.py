from pwn import *
import subprocess

CHAL = "shredder"

p = remote("ctfworkshop.cybr.club", 3003)

# automate inputs as necessary here

p.interactive()
