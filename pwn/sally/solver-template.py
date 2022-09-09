from pwn import *
import subprocess

CHAL = "sally"

p = remote("ctfworkshop.cybr.club", 3006, ssl=False)

# automate inputs as necessary here

p.interactive()
